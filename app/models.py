from flask import jsonify
from app.db import Database
from datetime import date
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash
import re

db_content = Database()


class User:

    def register_user(self, firstname, lastname, email, phonenumber, username,
                      othername, password):
        isAdmin = False
        registered = str(date.today())

        if not firstname.isalpha() or len(firstname) < 2 or " " in firstname:
            return jsonify({"message": "wrong first name format"}), 400

        if not lastname.isalpha() or len(lastname) < 2 or " " in lastname:
            return jsonify({"message": "wrong last name format"}), 400

        if not phonenumber.isdigit() or len(phonenumber) < 7 or " " in \
                phonenumber:
            return jsonify({"message": "wrong phone number format"}), 400

        if not othername.isalpha() or len(othername) < 2 or " " in othername:
            return jsonify({"message": "wrong other name format"}), 400

        email_format = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\. \
                                [a-z0-9-]+)*(\.[a-z]{2,4})$', email)
        if email_format is None:
            return jsonify({'error': 'Incorrect email format'})

        if len(username) < 5 or " " in username:
            return jsonify({"message": "wrong user name format"}), 400

        if self.check_user(username) is True:
            return jsonify({'message': 'Username already exists'})
    
        try:
            sql = "INSERT INTO users(firstname,lastname,email,phonenumber,\
                                    username,othername,password,registered \
                                    ,isAdmin) VALUES (%s,%s,%s,%s,%s,%s,%s, \
                                                        %s,%s)"
            db_content.cur.execute(sql, (firstname, lastname, email,
                                         phonenumber, username, othername,
                                         password, registered, isAdmin))
        except psycopg2.Error as err:
            return jsonify({'error': str(err)})
        return jsonify({'message': 'succussfully registered'}), 201

    def get_users(self):
        db_content.dict_cursor.execute("SELECT * FROM users")
        data = db_content.dict_cursor.fetchall()
        return jsonify({'users': data})
    
    def check_user(self, username):
        db_content.cur.execute("SELECT username from users")
        user_info = db_content.cur.fetchall()
        for user in user_info:
            if user[0] == username:
                return True
        return False


class Incident:

    def create_red_flag_record(self, createdBy, location, comment, images,
                               videos):
        status = "Draft"
        createdOn = str(date.today())
        incident_type = "red-flag"

        try:
            sql = "INSERT INTO incidents(createdOn,createdBy,incident_type,\
                                         location,status,comment,images,videos\
                                            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            db_content.cur.execute(sql, (createdOn, createdBy, incident_type,
                                         location, status, comment, images,
                                         videos))
        except psycopg2.Error as err:
            return jsonify({'error': str(err)})
        return jsonify({"status": 201, "data": [{"message": "Created red-flag\
                                                record"}]}), 201

    def get_all_redflags(self):
        db_content.dict_cursor.execute("SELECT * FROM incidents")
        data = db_content.dict_cursor.fetchall()
        return jsonify({'red-flags': data}), 200

    def update_redflag_comment(self, id, comment):
        sql = "UPDATE incidents SET comment='"+comment+"' WHERE id='{}'\
               ".format(id)
        db_content.cur.execute(sql)
        return jsonify({"status": 200, "data": [{"message": "Updated red-flag\
                         record's comment"}]}), 200

    def update_redflag_location(self, id, location):
        sql = "UPDATE incidents SET location='"+location+"' WHERE id='{}'\
                ".format(id)
        db_content.cur.execute(sql)
        return jsonify({"status": 200, "data": [{"message": "Updated red-flag\
                         record's location"}]}), 200

    def get_red_flag(self, id):
        db_content.dict_cursor.execute("SELECT * from incidents WHERE id='{}'\
                                       ".format(id))
        data = db_content.dict_cursor.fetchall()
        return jsonify({"status": 200, "data": data}), 200

    def delete_redflag(self, id):
        sql = "DELETE from incidents WHERE id='{}'".format(id)
        db_content.cur.execute(sql)
        return jsonify({"status": 200, "message": "Redflag deleted"})
