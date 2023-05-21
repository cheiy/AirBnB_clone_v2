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


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python(text=None):
    '''
    Function displays "Python" followed by the value of the text
    variable
    '''
    if text is None:
        text = "is cool"
        return 'Python %s' % text
    else:
        text = text.replace("_", " ")
        return 'Python %s' % text


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    '''
    Function displays the value n only if it's an integer
    '''
    return "%d is a number" % n


if __name__ == "__main__":
    app.run(host='0.0.0.0')
