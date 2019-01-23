from flask import jsonify, request, make_response
from app.models import Users
from instance import myapp
from werkzeug.security import generate_password_hash, check_password_hash
from app.db import Database
import jwt
import datetime


user1 = Users()
db_cont = Database()


@myapp.route('/api/v1/users', methods=['POST'])
def register_user():

    try:
        firstname = request.json['firstname']
        lastname = request.json['lastname']
        email = request.json['email']
        password = generate_password_hash(request.json['password'], method='sha256')
        phonenumber = request.json['phonenumber']
        username = request.json['username']
        othername = request.json['othername']
    except KeyError:
        return jsonify({'message': 'some fields are missing'}), 400   
    return user1.register_user(firstname, lastname, email, phonenumber, username, othername, password)


@myapp.route('/api/v1/users', methods=['GET'])
def get_users():

    return user1.get_users()


@myapp.route('/login', methods=['GET'])
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify')

    sql = "SELECT username, password, user_id from users WHERE username = %s"
    db_cont.dict_cursor.execute(sql, (auth.username,))
    user = db_cont.dict_cursor.fetchone()
    if not user:
        return make_response('Could not verif')
    if check_password_hash((user['password']), auth.password):
        token = jwt.encode({'user_id': user['user_id'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, myapp.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')})
    return make_response('Could not verify')
