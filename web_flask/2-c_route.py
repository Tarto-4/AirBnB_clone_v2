#!/usr/bin/python3
"""
Flask application demonstrating routes with variable and text processing.

This script defines a Flask application that listens on 0.0.0.0 port 5000
and displays greetings based on different routes:
  * "/": Displays "Hello HBNB!"
  * "/hbnb": Displays "HBNB"
  * "/c/<text>": Displays "C " followed by the provided text with underscores replaced by spaces.
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


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Displays "C " followed by the text variable with underscores replaced by spaces.
    """
    return f"C {text.replace('_', ' ')}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
