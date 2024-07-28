#!/usr/bin/python3
"""
index and home pages in the website
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def main():
    """ our index page """
    return "<p>Hello HBNB!</p>"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ the home page of HBNB"""
    return "<p>HBNB</P>"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    the c page to print whatever you wanna asy about C
    which is in the variable `text`
    """
    return "<p>C {}</p>".format(text.replace(' ', '_'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
