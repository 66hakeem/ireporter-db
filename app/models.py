from flask import jsonify
from app.db import Database
from datetime import date
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash


db_content = Database()

class Users:

    def register_user(self, firstname, lastname, email, phonenumber, username,
                      othername, password ):
        
        isAdmin = False
        registered = str(date.today())
        try:
            sql="INSERT INTO users(firstname,lastname,email,phonenumber,username,othername,password,registered,isAdmin) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            db_content.cur.execute(sql,(firstname,lastname,email,phonenumber,username,othername,password,registered,isAdmin))
        except psycopg2.Error as err:
            return jsonify({'error':str(err)})        
        return jsonify({'message':'succussfully registered'}),201
    

    def get_users(self):
        db_content.dict_cursor.execute("SELECT * FROM users")
        data=db_content.dict_cursor.fetchall() 
        return jsonify({'results':data})
"""
class Records:
    
    def create_red_flag_record(self, createdBy, location, comment, images,
                               videos, ):

        
        
    def get_red_flags(self):
        return jsonify({"status": 200, "data": self.records}), 200

    def get_red_flag(self, record_id):
        for record in self.records:
            if record['id'] == record_id:
                return jsonify({"status": 200, "data": record}), 200
            return jsonify({"message": "Record does not exist"})

    def delete_red_flag(self, record_id):
        for record in self.records:
            if record['id'] == record_id:
                self.records.remove(record)
                return jsonify({"status": 200, "data": [{"id": record_id,
                                "message": "red-flag record has been deleted"}]
                                }), 200

    def edit_redflag_location(self, record_id, location):
        for record in self.records:
            if record['id'] == record_id:
                record['location'] = location
                return jsonify({"status": 200, "data": [{"id": record_id,
                                "message": "Updated red-flag record's location"
                                                         }]}), 200

    def edit_redflag_comment(self, record_id, comment):
        for record in self.records:
            if record['id'] == record_id:
                record['comment'] = comment
                return jsonify({"status": 200, "data": [{"id": record_id,
                                "message": "Updated red-flag record's comment"}
                                                        ]}), 200

    def edit_redflag(self, record_id, location, comment, images, videos):
        for record in self.records:
            if record['id'] == record_id:
                record['location'] = location
                record['comment'] = comment
                record['images'] = images
                record['videos'] = videos

                return jsonify({"status": 200, "message":
                                "Updated red-flag"}), 200
"""