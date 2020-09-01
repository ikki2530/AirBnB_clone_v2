#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask
from flask import render_template
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

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_cool(text="is cool"):
    """return Python is cool by default"""
    new = text.replace("_", " ")
    return 'Python {}'.format(new)

@app.route('/number/<int:n>', strict_slashes=False)
def numb(n):
    """return n is a number"""
    if isinstance(n, int):
        return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def temp(n):
    """return a template"""
    if isinstance(n, int):
        return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)