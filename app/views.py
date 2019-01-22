from flask import jsonify, request
from app.models import Users
from instance import myapp
from werkzeug.security import generate_password_hash, check_password_hash


user1 = Users()


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
         return jsonify({'message':'some fields are missing'}),400   
    return user1.register_user(firstname, lastname, email, phonenumber, username, othername, password)

@myapp.route('/api/v1/users', methods=['GET'])
def get_users():

    return user1.get_users()