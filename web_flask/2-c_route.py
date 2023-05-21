#!/usr/bin/python3
'''
This script starts a Flask web application.
'''


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''
    Function returns the greeting text
    'Hello HBNB'
    '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''
    Function displays "HBNB"
    '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    '''
    Function displays the text passed in URL
    '''
    text = text.replace("_", " ")
    return 'C %s' % text


if __name__ == "__main__":
    app.run(host='0.0.0.0')
