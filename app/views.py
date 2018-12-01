from flask import jsonify, request
from models import Users
from instance import myapp

user1 = Users()

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