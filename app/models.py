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
        return jsonify({"status": 201, "data": [{"id":user_id, "message":"Created user."}]}), 201
    
    def get_users(self):
        """ gets a list of users"""
        return jsonify({"status": 200, "data": self.users}), 200

class Records:
    def __init__(self):
        self.records = []

    def create_red_flag_record(self, createdBy, location, comment, images, videos):
        record_id = len(self.records) + 1
        status = "Draft"
        created_on = str(date.today())
        record_type = "red-flag"

        record = {
            "id": record_id,
            "createdOn": created_on,
            "createdBy": createdBy,
            "type": record_type,
            "location": location,
            "status": status,
            "comment": comment,
            "images": images,
            "videos": videos
        }

        self.records.append(record)
        return jsonify({"status": 201, "data": [{"id":record_id, "message":"Created red-flag record"}]}),201
    
    def get_red_flags(self):
        """ gets a list of users"""
        return jsonify({"status": 200, "data": self.records}), 200
    
    def get_red_flag(self, record_id):
        """get a specific red flag"""
        for record in self.records:
            if record['id'] == record_id:
                return jsonify({"status":200, "data": record}), 200
    
    def delete_red_flag(self, record_id):
        """deletes a red flag record"""
        for record in self.records:
            if record['id'] == record_id:
                self.records.remove(record)
                return jsonify({"status":200, "data": [{"id":record_id, "message":"red-flag record has been deleted"}]}), 200
    
    def edit_redflag_location(self, record_id, location):
        """Edit a red-flag's location"""
        for record in self.records:
            if record['id'] == record_id:
                record['location'] = location
                return jsonify({"status": 200, "data": [{"id":record_id, "message":"Updated red-flag record's location"}]}), 200
    
    def edit_redflag_comment(self, record_id, comment):
        """Edit a red-flag's location"""
        for record in self.records:
            if record['id'] == record_id:
                record['comment'] = comment
                return jsonify({"status": 200, "data": [{"id":record_id, "message":"Updated red-flag record's comment"}]}), 200