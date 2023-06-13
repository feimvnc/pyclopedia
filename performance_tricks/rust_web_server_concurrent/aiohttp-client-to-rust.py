import aiohttp
import asyncio


from time import perf_counter
import asyncio
import aiohttp

async def fetch(s,  url):
    async with s.get(f'http://127.0.0.1:7878/') as r:
        if r.status != 200:
            r.raise_for_status()
        return await r.text()


async def fetch_all(s, urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(fetch(s, url))
        tasks.append(task)

    res = await asyncio.gather(*tasks)
    return res

'''
async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get('http://127.0.0.1:8080/') as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")
'''

async def main():
    urls = range(1, 10000)
    async with aiohttp.ClientSession() as session:
        htmls = await fetch_all(session, urls)
       #         print(htmls)


start = perf_counter()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
stop = perf_counter()
print('time taken:', stop - start)


