#!/usr/bin/python3
"""Flask app with basic routes and text handling."""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """Returns 'Hello HBNB!'"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns 'HBNB'"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Returns 'C <text>' with underscores replaced by spaces."""
    return f'C {text.replace("_", " ")}'

@app.route('/python/<text>', defaults={'text': 'is cool'}, strict_slashes=False)
def python_text(text):
    """Returns 'Python <text>' with underscores replaced by spaces (default: 'is cool')."""
    return f'Python {text.replace("_", " ")}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
