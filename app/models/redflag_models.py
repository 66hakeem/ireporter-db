from flask import jsonify
from app.db import Database
from datetime import date
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash
import re

db_content = Database()


class Redflag:

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
        db_content.dict_cursor.execute("SELECT * FROM incidents WHERE\
         incident_type='red-flag'")
        data = db_content.dict_cursor.fetchall()
        return jsonify({'red-flags': data}), 200

    def update_redflag_comment(self, id, comment):
        sql = "UPDATE incidents SET comment='"+comment+"' WHERE incident_type='red-flag' and incident_id='{}'\
               ".format(id)
        db_content.cur.execute(sql)
        return jsonify({"status": 200, "data": [{"message": "Updated red-flag\
                         record's comment"}]}), 200

    def update_redflag_location(self, id, location):
        sql = "UPDATE incidents SET location='"+location+"' WHERE incident_type='red-flag' and incident_id='{}'\
                ".format(id)
        db_content.cur.execute(sql)
        return jsonify({"status": 200, "data": [{"message": "Updated red-flag\
                         record's location"}]}), 200

    def get_red_flag(self, id):
        db_content.dict_cursor.execute("SELECT * from incidents WHERE incident_type='red-flag' and incident_id='{}'\
                                       ".format(id))
        data = db_content.dict_cursor.fetchall()
        return jsonify({"status": 200, "data": data}), 200

    def delete_redflag(self, id):
        sql = "DELETE from incidents WHERE incident_type='red-flag' and incident_id='{}'\
        ".format(id)
        db_content.cur.execute(sql)
        return jsonify({"status": 200, "message": "Redflag deleted"})
