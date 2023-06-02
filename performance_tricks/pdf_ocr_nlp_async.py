import asyncio
import json
import os
import time
import functools
from typing import List, Any, Callable

import httpx
import pytesseract
import pdf2image

DEFAULT_CONCUR_REQ = 30
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
async def do_ocr_and_nlp(image) -> Any:
    text = pytesseract.image_to_string(image, output_type=pytesseract.Output.STRING)
    async with httpx.AsyncClient() as client: # [1]
        response = await client.post(url=API_URL, data=json.dumps({"text": text}))
        response.raise_for_status()
    return response.read()


async def read_image(image: Any, semaphore: asyncio.Semaphore) -> Any:
    async with semaphore: # [2]
        res = await do_ocr_and_nlp(image)
    return res


async def process_file(filepath: str) -> Any:
    # A semaphore manages an internal counter which is decremented by each acquire() call
    semaphore = asyncio.Semaphore(DEFAULT_CONCUR_REQ) # [3]
    """
    In order to perform OCR on a PDF file, I first need to convert it to a file.
    To do that I'm using pdf2image function convert_from_bytes, which returns a list
    of images corresponding to each page in the file.
    """
    # images = pdf2image.convert_from_bytes(filepath, dpi=200)
    images = pdf2image.convert_from_path(filepath)
    
    tasks = [
        read_image(
            image=image,
            semaphore=semaphore
        ) for image in images
    ]
    result = await asyncio.gather(*tasks) # [4]
    return result


@timer
async def read_dirs(dirpath: str) -> List:
    to_do = [process_file(f"{dirpath}/{file}") for file in os.listdir(dirpath)]
    to_do_iter = asyncio.as_completed(to_do) # [5]
    final_result = []
    for future in to_do_iter:
        final_result.append(await future)
    return final_result


if __name__ == '__main__':
    t1 = time.perf_counter()
    result = asyncio.run(read_dirs(DIR_PATH))
    t2 = time.perf_counter() - t1
    print(t2)
    # print(result)
