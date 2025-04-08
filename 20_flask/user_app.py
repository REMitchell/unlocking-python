import hashlib
import sqlite3
from flask import Flask, request

'''
CREATE TABLE Users(
	user_id INTEGER PRIMARY KEY AUTOINCREMENT,
	first_name VARCHAR(32),
	last_name VARCHAR(32),
	username VARCHAR(32),
	email VARCHAR(64),
    password_hash VARCHAR(32),
	last_login DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO Users 
(first_name, last_name, username, email, password_hash, last_login)
VALUES
    ('Alice', 'Acevedo', 'alice123', 'a@example.com', NULL, '2024-01-01 12:00:00'),
    ('Bob', 'Brown', 'bobby_brown', 'b@example.com', NULL, '2024-02-01 12:00:00'),
    ('Charlie', 'Clark', 'chuck', 'c@example.com', NULL, '2024-03-01 12:00:00');
'''

app = Flask(__name__)


# Only one endpoint at a time can be connected to '/user'
# The first two examples are commented out

#@app.route('/user', methods=['GET'])
#def get_user_by_id():
#    with sqlite3.connect('unlocking-python.db') as conn:
#        cur = conn.cursor()
#        fetch_query = f'''
#            SELECT 
#                user_id, first_name, last_name, username, email, last_login
#            FROM Users 
#            WHERE user_id = {request.args.get('user_id')}
#        '''
#        cur.execute(fetch_query)
#        return cur.fetchall()


#@app.route('/user')
#def get_user_by_id():
#    with sqlite3.connect('unlocking-python.db') as conn:
#        cur = conn.cursor()
#        fetch_query = f''' SELECT
#            user_id, first_name, last_name, username, email, last_login 
#            FROM Users
#            WHERE user_id = ?
#        '''
#        cur.execute(fetch_query, (request.args.get('user_id'),))
#        return cur.fetchall()


@app.route('/user', methods=['POST'])
def create_user():
    with sqlite3.connect('unlocking-python.db') as conn:
        cur = conn.cursor()
        data = request.json
        insert_query = '''
            INSERT INTO Users (
                first_name, last_name, username, email
            )
            VALUES
            (?, ?, ?, ?)
            '''
        cur.execute(insert_query, (
            data.get('first_name'),
            data.get('last_name'),
            data.get('username'),
            data.get('email')
        ))
        conn.commit()
        return {'id': cur.lastrowid}

## AUTHENTICATION ##

# Note that we should be using something more secure, such as bcrypt, as well as a salt
# However, SHA256 works out of the box in Python, and it's fine


# >>> hashlib.sha256('asdf'.encode('utf-8')).hexdigest()
# 'f0e4c2f76c58916ec258f246851bea091d14d4247a2fc3e18694461b1816e13b'


'''
UPDATE Users SET 
password_hash='5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'
'''
from werkzeug.exceptions import BadRequest, Unauthorized
import hashlib
from flask import make_response

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return BadRequest('Must provide username and password to log in')
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    match_query = f'''
        SELECT user_id FROM Users 
        WHERE username = ?
        AND password_hash = ?
    '''
    with sqlite3.connect('unlocking-python.db') as conn:
        cur = conn.cursor()
        cur.execute(match_query, (username, password_hash))
        user_id = cur.fetchone()
        if user_id:
            user_id = user_id[0]
            session = create_session(user_id, conn)
            resp = make_response({'id': user_id})
            resp.set_cookie('session_id', session)
            return resp
        return Unauthorized('Authentication failed')


## SESSIONS ##

from flask import Flask, request, session

app.secret_key = 'CHANGE_ME'

@app.route('/set-session-data', methods=['GET'])
def set_session_data():
    data = request.args.get('data')
    session['data'] = data
    return f'Set session data: {data}'

@app.route('/get-session-data', methods=['GET'])
def get_session_data():
    if 'data' not in session:
        return 'No session data set'
    return f'Session data is: {session['data']}'


'''
CREATE TABLE Sessions(
    user_id INTEGER PRIMARY KEY,
    session_id VARCHAR(64),
    expiration_date DATETIME
);
'''

'''
INSERT INTO Sessions (user_id)
    SELECT user_id FROM Users;
'''
import uuid 
from datetime import datetime, timedelta

def create_session(user_id, conn):
    session_id = uuid.uuid1().hex
    session_query = f'''
        UPDATE Sessions
        SET session_id = ?, expiration_date = ?
        WHERE user_id = ?
    '''
    print(session_query)
    cur = conn.cursor()
    cur.execute(session_query, (
        session_id,
        datetime.today() + timedelta(days=1),
        int(user_id),
    ))
    return session_id


def authorize_request(conn):
    session_id = request.cookies.get('session_id')
    if not session_id:
        return None
    authorize_query = f'''
    SELECT user_id FROM Sessions
    WHERE session_id = ?
    AND expiration_date > CURRENT_TIMESTAMP
    '''
    cur = conn.cursor()
    cur.execute(authorize_query, (session_id,))
    user_id = cur.fetchone()
    if user_id:
        return user_id[0]
    return None


@app.route('/whoami')
def whoami():
    with sqlite3.connect('unlocking-python.db') as conn:
        return {'user_id': authorize_request(conn)}

## TEMPLATES ##

class User:
    def __init__(self, data):
        self.first_name = data[0]
        self.last_name = data[1]
        self.username = data[2]
        self.email = data[3]

from flask import render_template

@app.route('/profile', methods=['GET'])
def profile():
    with sqlite3.connect('unlocking-python.db') as conn:
        user_id = authorize_request(conn)
        if not user_id:
            return Unauthorized('Need to log in')
        user_query = f'''
            SELECT first_name, last_name, username, email
            FROM Users
            WHERE user_id = ?
        '''
        cur = conn.cursor()
        cur.execute(user_query, (int(user_id),))
        user = User(cur.fetchone())
    return render_template('profile.html', user=user)




