#!/usr/bin/python3
'''
This script starts a Flask web application.
'''


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''
    Function returns the text
    '''
    return 'Hello, HBNB!'
