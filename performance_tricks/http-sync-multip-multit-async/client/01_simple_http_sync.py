import requests
import timeit 

def timer(number, repeat):
    def wrapper(func):
        runs = timeit.repeat(func, number=number, repeat=repeat)
        print(sum(runs) / len(runs))
    return wrapper



url = 'http://localhost:7878/'

def  fetch(session, url):
    with session.get(url) as response:
        #print(response)
        pass

@timer(1, 1)
def main():
    with requests.Session() as session:
        for _ in range(5000):
            fetch(session, url)


