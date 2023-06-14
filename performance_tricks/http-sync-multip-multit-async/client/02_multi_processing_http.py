import requests
import timeit 
from multiprocessing.pool import Pool

url = 'http://localhost:7878/'

def fetch(session, url):
    with session.get(url) as response:
        #print(response)
        pass

def timer(number, repeat):
    def wrapper(func):
        runs = timeit.repeat(func, number=number, repeat=repeat)
        print(sum(runs) / len(runs))
    return wrapper

if __name__ ==  "__main__":

    @timer(1, 1)
    def task():
        with Pool() as pool:
            with requests.Session() as session:
                pool.starmap(fetch, [(session, url) for _ in range(5000)])


