from typing import Union
import random, string

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
async def read_item(item_id: int, q: Union[str, None] = None):
    #return {"item_id": item_id, "q": q}
    #print(item_id)
    num = ''.join(random.choices(string.ascii_lowercase, k=5))
    return {'data': num, 'num': item_id}
