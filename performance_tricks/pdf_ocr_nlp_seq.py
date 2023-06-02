import time
import functools
import os
from typing import List, Any, Callable
import pytesseract
import pdf2image
import httpx
import json 



API_URL = "http://localhost:8080/2017-attention-is-all-you-need-Paper.pdf"
DIR_PATH = './pdf_files'

# Timer function to be used as a decorator
def timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elsaped = time.perf_counter() - start
        print(f'Took us [{elsaped:.2f}s] to run [{func.__name__}]')
        return result
    return wrapper

# OCR and NLP Logics
def do_ocr_and_nlp(image: Any):
    text = pytesseract.image_to_string(
        image,
        output_type=pytesseract.Output.STRING
    )
    with httpx.Client() as client:
        response = client.post(url=API_URL, data=json.dumps({"text": text}))
        response.raise_for_status()
    return response.read()
        

def process_file(filepath: str) -> List:
    # images = pdf2image.convert_from_bytes(filepath, dpi=200)
    images = pdf2image.convert_from_path(filepath)

    res = []
    for image in images:
        res.append(do_ocr_and_nlp(image))
    return res

@timer
def read_dir(dirpath: str) -> List:
    files = os.listdir(dirpath)
    final_result = []
    if len(files) > 0:
        for file in files:
            filepath = os.path.join(dirpath, file)
            final_result.append(process_file(filepath))
    return final_result

@timer
async def read_dirs(dirpath: str) -> List:
    to_do_iter = [process_file(f"{dirpath}/{file}") for file in os.listdir(dirpath)]
    # to_do_iter = asyncio.as_completed(to_do) # [5]
    final_result = []
    for future in to_do_iter:
        final_result.append(await future)
    return final_result
    
if __name__ == '__main__':
    t1 = time.perf_counter()
    result = read_dir(DIR_PATH)
    t2 = time.perf_counter() - t1
    print(t2)
    # print(result)
