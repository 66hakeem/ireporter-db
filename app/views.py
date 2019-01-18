from flask import jsonify, request
from app.models import Users, Records
from instance import myapp

user1 = Users()
record1 = Records()


@myapp.route('/api/v1/users', methods=['POST'])
def register_user():
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    email = request.json['email']
    phonenumber = request.json['phonenumber']
    username = request.json['username']
    othername = request.json['othername']
    return user1.register_user(firstname, lastname, email, phonenumber,
                               username, othername)


@myapp.route('/api/v1/users', methods=['GET'])
def get_users():
    return user1.get_users()


@myapp.route('/api/v1/red_flags', methods=['POST'])
def create_red_flag():
    createdBy = request.json['createdBy']
    location = request.json['location']
    comment = request.json['comment']
    images = []
    images.append(request.json['images'])
    videos = []
    videos.append(request.json['videos'])

    return record1.create_red_flag_record(createdBy, location, comment, images,
                                          videos)


@myapp.route('/api/v1/red_flags', methods=['GET'])
def get_red_flag_records():
    return record1.get_red_flags()


@myapp.route('/api/v1/red_flags/<int:red_flag_id>', methods=['GET'])
def get_specific_redflag(red_flag_id):
    return record1.get_red_flag(red_flag_id)


@myapp.route('/api/v1/red_flags/<int:red_flag_id>', methods=['DELETE'])
def delete_redflag_records(red_flag_id):
    return record1.delete_red_flag(red_flag_id)


@myapp.route('/api/v1/red_flags/<int:red_flag_id>/location', methods=['PATCH'])
def edit_location(red_flag_id):
    location = request.json['location']
    return record1.edit_redflag_location(red_flag_id, location)


@myapp.route('/api/v1/red_flags/<int:red_flag_id>/comment', methods=['PATCH'])
def edit_comment(red_flag_id):
    comment = request.json['comment']
    return record1.edit_redflag_comment(red_flag_id, comment)


@myapp.route('/api/v1/red_flags/<int:red_flag_id>', methods=['PUT'])
def edit_red_flag(red_flag_id):
    location = request.json['location']
    comment = request.json['comment']
    images = []
    images.append(request.json['images'])
    videos = []
    videos.append(request.json['videos'])

    return record1.edit_redflag(red_flag_id, location, comment, images, videos)
