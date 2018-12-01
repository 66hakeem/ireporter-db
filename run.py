from instance import myapp
from app import views

if __name__==('__main__'):
    myapp.run(debug=True, port=5000)