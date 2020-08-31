#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask
from flask import escape


app = Flask(__name__)
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """function for root /"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """function for /hbnb url"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_isfun(text):
    """return C is fun"""
    new = text.replace("_", " ")
    return 'C {}'.format(new)

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000)
