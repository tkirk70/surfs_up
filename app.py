# import the dependencies.
from flask import Flask

# Adding a flask 'instance' or singular version of something.
app = Flask(__name__)

# Define starting point or root.
@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/data')
def data():
    return 'Oahu Weather Data Under Construction.  Stay tuned for updates.'
