from fastapi import FastAPI
import string 
import random 

app = FastAPI()

@app.get('/')
async def index():
    num = ''.join(random.choices(string.ascii_lowercase, k=5))
    return {'data': num}

@app.get('/items/{item_id}')
async def read(item_id: int):
    return {'item_id': item_id}


