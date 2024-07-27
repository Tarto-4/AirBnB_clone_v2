# __init__.py
from flask import Flask, render_template, request
from models import storage

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

# Import and register blueprint for each task
