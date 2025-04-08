from flask import Flask, request

app = Flask(__name__)


@app.route('hello')
def hello_world():
    return 'Hello, World!'


@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>Hello World Page</title>
        </head>
        <body>
            <h1>Spanish Inquisition</h1>
            <p>
            In the early years of the 16th century, to combat the rising tide of religious unorthodoxy, the Pope gave Cardinal Ximinez of Spain leave to move without let or hindrance throughout the land, in a reign of violence, terror and torture that makes a smashing film. This was the Spanish Inquisition...
            </p>
        </body>
    </html>    
    '''


from flask import request
from werkzeug.exceptions import BadRequest


# http://127.0.0.1:5000/profile?first_name=Ryan&last_name=Mitchell
@app.route('/profile')
def profile():
    if not (request.args.get('first_name') and request.args.get('last_name')):
        return BadRequest('Missing required parameters first_name and last_name')
    name = f'{request.args.get("first_name")} {request.args.get("last_name")}'
    return f'<html><body><h1>{name}</h1></body></html>'


@app.route('/profile/<firstname>/<lastname>')
def profile_path(firstname, lastname):
    return f'<html><body><h1>{firstname} {lastname}</h1></body></html>'


@app.route('/profile/default/page')
def profile_default():
    return f'<html><body><h1>DEFAULT</h1></body></html>'


import math

@app.route('/factorial')
def factorial():
    num = int(request.args.get('num', 0))
    return {'factorial': math.factorial(num), 'num': num}


from flask import jsonify

@app.route('/lessthan')
def lessthan():
    num = int(request.args.get('num', 0))
    return [i for i in range(num)]


class User:
    def __init__(self):
        self.user_id = 1
        first_name = 'Ryan'
        last_name = 'Mitchell'
        username = 'remitchell'
        email = 'ryan@ryanemitchell.com'
        password_hash = None
        last_login = None

    def to_dict(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'email': self.email,
        }


def serialize_json(obj):
    if type(obj) == User:
        return obj.to_dict()
    return obj


@app.route('/user')
def user():
    u = User()
    return jsonify(u, default=serialize_json)


@app.route('/headers', methods=['GET', 'POST'])
def headers():
    print(request.headers)

    return {'headers': request.headers.get('Content-Type')}
