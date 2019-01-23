import psycopg2
from psycopg2.extras import RealDictCursor


class Database:

    con = psycopg2.connect(host="ec2-54-235-77-0.compute-1.amazonaws.com", database="d85rsjln3lp2ki",
                           user="jpgnpigszjngpj", password="063c9c7bec6c3cfad17726089c634858f17b0d94b049a996afe43705a6a225b5", port="5432")

    dict_cursor = con.cursor(cursor_factory=RealDictCursor)
    cur = con.cursor()
    con.autocommit = True

    def create_tables(self):
        user_table = """create table if not exists users(
            user_id serial PRIMARY KEY NOT NULL,
            firstname VARCHAR(50) NOT NULL, 
            lastname VARCHAR(50) NOT NULL,
            othername VARCHAR(50) NOT NULL,
            username VARCHAR(50) NOT NULL,
            email VARCHAR(50) NOT NULL,
            phonenumber int NOT NULL,
            password TEXT NOT NULL,
            registered DATE NOT NULL,
            isAdmin BOOL NOT NULL )"""
        incidents_table = """create table if not exists incidents(
            id serial NOT NULL,
            createdOn DATE NOT NULL,
            createdBy VARCHAR(50) NOT NULL,
            incident_type VARCHAR(50) NOT NULL,
            location VARCHAR(50) NOT NULL,
            status VARCHAR (50) NOT NULL,
            comment VARCHAR (50) NOT NULL,
            images VARCHAR (50) NOT NULL,
            videos VARCHAR (50) NOT NULL )"""

        Database.cur.execute(user_table)
        Database.cur.execute(incidents_table)

    def drop_tables(self):

        drop_tables = "DROP TABLE users, incidents"
        Database.cur.execute(drop_tables)

create = Database()
create.create_tables()  
