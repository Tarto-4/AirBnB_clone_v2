#!/usr/bin/python3
"""Flask web application with routes and text variable handling"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
  """Returns a message"""
  return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
  """Returns HBNB"""
  return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
  """Returns C text with replaced underscores"""
  text = text.replace('_', ' ')
  return f"C {text}"

@app.route('/python/<text>', defaults={'text': 'is cool'}, strict_slashes=False)
def python_is_cool(text):
  """Returns Python text with replaced underscores (default: is cool)"""
  text = text.replace('_', ' ')
  return f"Python {text}"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
