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
