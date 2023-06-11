from aiohttp import web
import random 
import string 

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
async def read_item(request):
    #return {"item_id": item_id, "q": q}
    #print(item_id)
    num = ''.join(random.choices(string.ascii_lowercase, k=5))
    return {'data': num, 'num': num}

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/item', read_item),
                web.get('/{name}', handle)])


if __name__ == '__main__':
    web.run_app(app)
