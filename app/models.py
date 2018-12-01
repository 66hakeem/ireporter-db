from flask import jsonify
from datetime import date


class Users:

    def __init__(self):
        self.users = []
    
    def register_user(self, firstname, lastname, email, phonenumber, username, othername = ''):
        """ functions adds a user to the users dictionary """
        user_id = len(self.users) + 1
        isAdmin = False
        today = str(date.today()) 

        user = {
            "firstname": firstname,
            "user_id": user_id,
            "lastname": lastname,
            "email": email,
            "phonenumber": phonenumber,
            "username": username,
            "othername": othername,
            "isAdmin": isAdmin,
            "registered": today
        }
        self.users.append(user)
        return jsonify({'message':'successfully added'}), 201
    
    def get_users(self):
        """ gets a list of users"""
        return jsonify({'users':self.users}),200