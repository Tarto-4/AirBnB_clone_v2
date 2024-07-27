#!/usr/bin/python3
"""
Flask application demonstrating a simple route.

This script defines a Flask application that listens on 0.0.0.0 port 5000
and displays "Hello HBNB!" when accessing the root URL (/).
"""

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays "Hello HBNB!" on the root path.
    """
    return "Hello HBNB!"
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
