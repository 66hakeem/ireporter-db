from flask import jsonify, request, make_response
from app.models.user_models import User
from app.models.redflag_models import Redflag
from app.models.intervention_models import Intervention
from instance import myapp
from werkzeug.security import generate_password_hash, check_password_hash
from app.db import Database
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, verify_jwt_in_request,
                                jwt_required)
import datetime
from functools import wraps

db_cont = Database()
jwt = JWTManager(myapp)


"""
def admin(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth = request.authorization
        userr = get_jwt_identity()
        sql = "SELECT username, isAdmin from users WHERE username = %s"
        db_cont.dict_cursor.execute(sql, (auth.username,))
        usere = db_cont.dict_cursor.fetchone()
        if usere['isAdmin'] == 'False':
            return jsonify({'msg': 'Admins only!'}), 403
        else:
            return f(*args, **kwargs)
    return wrapper
"""


@myapp.route('/api/v1/auth/login', methods=['POST'])
def login():
    """Login to your account"""
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json['username']
    password = request.json['password']

    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400
    
    sql = "SELECT username, password, user_id, isAdmin from users WHERE\
             username = %s"
    db_cont.dict_cursor.execute(sql, (username,))
    user = db_cont.dict_cursor.fetchone()
    if not user:
        return make_response('User not found')
    if check_password_hash((user['password']), password):
        access_token = create_access_token(identity=username)
        return jsonify({'token': access_token})
    return make_response('Wrong Password')


@myapp.route('/api/v1/users', methods=['POST'])
def register_user():
    """Create user"""
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
@jwt_required
def get_users():
    """Get all users"""
    return User().get_users()


@myapp.route('/api/v1/red_flags', methods=['POST'])
@jwt_required
def create_red_flag():
    """Create a red-flag"""
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
@jwt_required
def get_red_flags():
    """Get all red-flags"""
    return Redflag().get_all_redflags()


@myapp.route('/api/v1/red_flags/<int:red_flag_id>/comment', methods=['PATCH'])
@jwt_required
def update_red_flag_comment(red_flag_id):
    """Update red-flag comment"""
    try:
        comment = request.json['comment']
    except KeyError:
        return jsonify({'message': 'Comment field is missing'}), 400

    return Redflag().update_redflag_comment(red_flag_id, comment)


@myapp.route('/api/v1/red_flags/<int:red_flag_id>/location', methods=['PATCH'])
@jwt_required
def update_location(red_flag_id):
    """Update red-flag location"""
    try:
        location = request.json['location']
    except KeyError:
        return jsonify({'message': 'Location field is missing'}), 400
    
    return Redflag().update_redflag_location(red_flag_id, location)


@myapp.route('/api/v1/red_flags/<int:red_flag_id>/status', methods=['PATCH'])
@jwt_required
def update_status(red_flag_id):
    """Update red-flag status"""
    try:
        status = request.json['status']
    except KeyError:
        return jsonify({'message': 'Status field is missing'}), 400
    
    return Redflag().update_redflag_status(red_flag_id, status)


@myapp.route('/api/v1/red_flags/<int:red_flag_id>', methods=['GET'])
@jwt_required
def get_specific_redflag(red_flag_id):
    """Get a specific red-flag"""
    return Redflag().get_red_flag(red_flag_id)


@myapp.route('/api/v1/red_flags/<int:red_flag_id>', methods=['DELETE'])
@jwt_required
def delete_redflag_record(red_flag_id):
    """Delete a specific red-flag"""
    return Redflag().delete_redflag(red_flag_id)


@myapp.route('/api/v1/intervention', methods=['POST'])
@jwt_required
def create_intervention():
    """Create an intervention record"""
    try:
        createdBy = get_jwt_identity()
        location = request.json['location']
        comment = request.json['comment']
        images = request.json['images']
        videos = request.json['videos']
    except KeyError:
        return jsonify({'message': 'some fields are missing'}), 400
    return Intervention().create_intervention_record(createdBy, location, 
                                                     comment, images, videos)


@myapp.route('/api/v1/interventions', methods=['GET'])
@jwt_required
def get_interventions():
    """Get all intervention records"""
    return Intervention().get_all_interventions()


@myapp.route('/api/v1/intervention/<int:intervention_id>', methods=['GET'])
@jwt_required
def get_specific_intervention(intervention_id):
    """Get a specific intervention"""
    return Intervention().get_intervention(intervention_id)


@myapp.route('/api/v1/intervention/<int:intervention_id>/comment',
             methods=['PATCH'])
@jwt_required
def update_intervention_comment(intervention_id):
    """Update an intervention record's comment"""
    try:
        comment = request.json['comment']
    except KeyError:
        return jsonify({'message': 'Comment field is missing'}), 400

    return Intervention().update_intervention_comment(intervention_id, comment)


@myapp.route('/api/v1/intervention/<int:intervention_id>/location',
             methods=['PATCH'])
@jwt_required
def update_intervention_location(intervention_id):
    """Update intervention location"""
    try:
        location = request.json['location']
    except KeyError:
        return jsonify({'message': 'Location field is missing'}), 400

    return Intervention().update_intervention_location(intervention_id,
                                                       location)


@myapp.route('/api/v1/intervention/<int:intervention_id>', methods=['DELETE'])
@jwt_required
def delete_intervention_record(intervention_id):
    """Delete a specific red-flag"""
    return Intervention().delete_intervention(intervention_id)


@myapp.route('/api/v1/intervention/<int:intervention_id>/status',
             methods=['PATCH'])
@jwt_required
def update_intervention_status(intervention_id):
    """Update an intervention record's status"""
    """
    user_logged = get_jwt_identity()
    sql = "SELECT username, isAdmin from users WHERE username = %s"
    db_cont.dict_cursor.execute(sql, (user_logged,))
    userr = db_cont.dict_cursor.fetchone()
    if userr['isAdmin'] == 'False':
        return jsonify({'msg': 'Admins only!'}), 403
    else:
    """
    status = request.json['status']
    return Intervention().update_intervention_status(intervention_id,
                                                     status)       
    

    