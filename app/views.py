from flask import jsonify, request, make_response
from app.models.user_models import User
from app.models.redflag_models import Redflag
from app.models.intervention_models import Intervention
from instance import myapp
from werkzeug.security import generate_password_hash, check_password_hash
from app.db import Database
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, jwt_required)
import datetime
from functools import wraps

db_cont = Database()
jwt = JWTManager(myapp)


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


@myapp.route('/api/v1/users', methods=['POST'])
def register_user():

    try:
        firstname = request.json['firstname']
        lastname = request.json['lastname']
        email = request.json['email']
        password = generate_password_hash(request.json['password'],
                                          method='sha256')
        phonenumber = request.json['phonenumber']
        username = request.json['username']
        othername = request.json['othername']
    except KeyError:
        return jsonify({'message': 'some fields are missing'}), 400
    return User().register_user(firstname, lastname, email, phonenumber,
                                username, othername, password)


@myapp.route('/api/v1/users', methods=['GET'])
def get_users():

    return User().get_users()


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
    return Redflag().create_red_flag_record(createdBy, location, comment,
                                            images, videos)


@myapp.route('/api/v1/red_flags', methods=['GET'])
def get_red_flags():

    return Redflag().get_all_redflags()


@myapp.route('/api/v1/red_flags/<int:red_flag_id>/comment', methods=['PATCH'])
def update_red_flag_comment(red_flag_id):
    try:
        comment = request.json['comment']
    except KeyError:
        return jsonify({'message': 'Comment field is missing'}), 400

    return Redflag().update_redflag_comment(red_flag_id, comment)


@myapp.route('/api/v1/red_flags/<int:red_flag_id>/location', methods=['PATCH'])
def update_location(red_flag_id):
    try:
        location = request.json['location']
    except KeyError:
        return jsonify({'message': 'Location field is missing'}), 400

    return Redflag().update_redflag_location(red_flag_id, location)


@myapp.route('/api/v1/red_flags/<int:red_flag_id>', methods=['GET'])
def get_specific_redflag(red_flag_id):
    return Redflag.get_red_flag(red_flag_id)


@myapp.route('/api/v1/red_flags/<int:red_flag_id>', methods=['DELETE'])
def delete_redflag_record(red_flag_id):
    return Redflag().delete_redflag(red_flag_id)


@myapp.route('/api/v1/interventions', methods=['GET'])
def get_interventions():

    return Intervention().get_all_interventions()


@myapp.route('/api/v1/intervention/<int:intervention_id>/comment',
             methods=['PATCH'])
def update_intervention_comment(intervention_id):
    try:
        comment = request.json['comment']
    except KeyError:
        return jsonify({'message': 'Comment field is missing'}), 400

    return Intervention().update_intervention_comment(intervention_id, comment)
