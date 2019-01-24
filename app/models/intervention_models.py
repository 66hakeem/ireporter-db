from flask import jsonify
from app.db import Database
from datetime import date
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash
import re

db_content = Database()


class Intervention:

    def create_intervention_record(self, createdBy, location, comment, images,
                                   videos):
        status = "Draft"
        createdOn = str(date.today())
        incident_type = "intervention"

        try:
            sql = "INSERT INTO incidents(createdOn,createdBy,incident_type,\
                                         location,status,comment,images,videos\
                                            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            db_content.cur.execute(sql, (createdOn, createdBy, incident_type,
                                         location, status, comment, images,
                                         videos))
        except psycopg2.Error as err:
            return jsonify({'error': str(err)})
        return jsonify({"status": 201, "data": [{"message": "Created intervention\
                                                record"}]}), 201

    def get_all_interventions(self):
        db_content.dict_cursor.execute("SELECT * FROM incidents WHERE\
         incident_type='intervention'")
        data = db_content.dict_cursor.fetchall()
        return jsonify({'interventions': data}), 200

    def update_intervention_comment(self, id, comment):
        sql = "UPDATE incidents SET comment='"+comment+"'\
         WHERE incident_type='intervention' and id='{}'\
               ".format(id)
        db_content.cur.execute(sql)
        return jsonify({"status": 200, "data": [{"message": "Updated intervention\
        record's comment"}]}), 200

    def update_intervention_location(self, id, location):
        sql = "UPDATE incidents SET location='"+location+"' WHERE\
         incident_type='intervention' and id='{}'".format(id)
        db_content.cur.execute(sql)
        return jsonify({"status": 200, "data": [{"message": "Updated\
         intervention record's location"}]}), 200

    def update_intervention_status(self, id, status):
        sql = "UPDATE incidents SET status='"+status+"' WHERE\
         incident_type='intervention' and id='{}'".format(id)
        db_content.cur.execute(sql)
        return jsonify({"status": 200, "data": [{"message": "Updated\
         intervention record's status"}]}), 200

    def get_intervention(self, id):
        db_content.dict_cursor.execute("SELECT * from incidents WHERE\
         incident_type='intervention' and id='{}'".format(id))
        data = db_content.dict_cursor.fetchall()
        return jsonify({"status": 200, "data": data}), 200

    def delete_intervention(self, id):
        sql = "DELETE from incidents WHERE incident_type='intervention'\
         and id='{}'".format(id)
        db_content.cur.execute(sql)
        return jsonify({"status": 200, "message": "Intervention deleted"})
