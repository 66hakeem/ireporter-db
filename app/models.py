from flask import jsonify
from datetime import date


class Users:

    def __init__(self):
        self.users = []
    
    def register_user(self, firstname, lastname, email, phonenumber, username, othername):
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

class Records:
    def __init__(self):
        self.records = []

    def create_red_flag_record(self, createdBy, location, comment, images=list()):
        record_id = len(self.records) + 1
        status = "Draft"
        created_on = str(date.today())
        record_type = "red-flag"

        images = []

        record = {
            "id": record_id,
            "createdOn": created_on,
            "createdBy": createdBy,
            "type": record_type,
            "location": location,
            "status": status,
            "comment": comment,
            "images": images
        }

        self.records.append(record)
        return jsonify({'message':'successfully added'}), 201
    
    def get_red_flags(self):
        """ gets a list of users"""
        return jsonify({'records':self.records}),200