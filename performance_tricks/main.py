import random 
import string

from flask import Flask, json, request

api = Flask(__name__)

@api.route('/item')
def get_items():
    name = request.args.get('num')
    print(name)
    num = ''.join(random.choices(string.ascii_lowercase, k=5))
    return {'data': num, 'num': name}

if __name__ == '__main__':
    api.run(debug=True)
