#!/usr/bin/python3
"""
Flask application demonstrating multiple routes with strict_slashes=False.

This script defines a Flask application that listens on 0.0.0.0 port 5000
and displays "Hello HBNB!" on the root path and "HBNB" on the /hbnb path.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays "Hello HBNB!" on the root path.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays "HBNB" on the /hbnb path.
    """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
