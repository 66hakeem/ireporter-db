from instance import myapp
from app import views
from app.db import Database

if __name__ == ('__main__'):
    myapp.run(port=5000)
    Database().create_tables()
