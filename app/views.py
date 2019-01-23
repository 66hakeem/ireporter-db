from flask import jsonify, request, make_response
from app.models import Users, Incidents
from instance import myapp
from werkzeug.security import generate_password_hash, check_password_hash
from app.db import Database
from flask_jwt_extended import (JWTManager, verify_jwt_in_request, jwt_required, create_access_token, get_jwt_identity)
import datetime
from functools import wraps

record = Incidents()
user1 = Users()
db_cont = Database()
jwt = JWTManager(myapp)


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
@jwt_required
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
        return make_response('User not found')
    if check_password_hash((user['password']), auth.password):
        token = create_access_token(identity=auth.username)
        return jsonify({'token': token})
    return make_response('Could not verify')

@myapp.route('/api/v1/red_flags', methods=['POST'])
@jwt_required
def create_red_flag():
    try:
        createdBy = get_jwt_identity()
        location = request.json['location']
        comment = request.json['comment']
        images = request.json['images']
        videos = request.json['videos']    
    except KeyError:
        return jsonify({'message': 'some fields are missing'}), 400 
    return record.create_red_flag_record(createdBy, location, comment, images, videos)
