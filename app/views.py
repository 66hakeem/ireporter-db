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
    return user1.register_user(firstname, lastname, email, phonenumber, username, othername)

@myapp.route('/api/v1/users', methods=['GET'])
def get_users():
    return user1.get_users()

@myapp.route('/api/v1/records', methods=['POST'])
def create_red_flag():
    createdBy = request.json['createdBy']
    location = request.json['location']
    comment = request.json['comment']
    images = []
    images.append(request.json['images'])
    videos = []
    videos.append(request.json['videos'])

    return record1.create_red_flag_record(createdBy, location, comment, images, videos)

@myapp.route('/api/v1/records', methods=['GET'])
def get_red_flag_records():
    return record1.get_red_flags()

@myapp.route('/api/v1/records/<int:record_id>', methods=['GET'])
def get_specific_redflag(record_id):
    return record1.get_red_flag(record_id)