#!/usr/bin/python3
"""
index, home, C, Python pages in the website
"""

from flask import Flask, render_template
from flask import abort

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def main():
    """ our index page """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ the home page of HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    the c page to print whatever you wanna asy about C
    which is in the variable `text`
    """
    return "C {}".format(text.replace('_', ' '))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_describe(text=None):
    """the python page to describe pit whatever you want"""
    return "Python {}".format(text.replace('_', ' ') if text else "is cool")


@app.route("/number/", strict_slashes=False)
@app.route("/number/<n>", strict_slashes=False)
def print_num(n=None):
    """ page for printing numbers only if there's number"""
    if n.isnumeric():
        return "{} is a number".format(n)
    else:
        abort(404)


@app.route("/number_template/", strict_slashes=False)
@app.route("/number_template/<n>", strict_slashes=False)
def number_page(n):
    """ returns the HTML psge only if n is number"""
    if n is not None and n.isnumeric():
        return render_template('5-number.html', n=n)
    else:
        return abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
