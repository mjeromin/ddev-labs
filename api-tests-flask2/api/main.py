#!/usr/bin/env python

from pyprimes import is_prime
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Prime API!"

@app.route('/prime/<int:n>', methods=['GET'])
def prime_test(n):
    if is_prime(n):
        return "This is prime: {}\n".format(n)
    else:
        return "This is not so prime: {}\n".format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
