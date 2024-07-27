#!/usr/bin/python3
"""
simple and first page in the website
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def main():
    """ our home page function """

    return "<p>Hello HBNB!</p>"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
