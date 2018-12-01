from flask import json
from unittest import TestCase
from app import views
from instance import myapp


class ApiTest(TestCase):
    def setUp(self):
        self.app = myapp.test_client()
    
    def test_registration(self):
        add_user = self.app.post('/api/v1/users', content_type='application/json',
        data=json.dumps(dict(firstname="hakeem", lastname="matovu", email="hakeem@gmail.com", 
        phonenumber="0781508582", username="hakeem66", othername="salim")))

        self.assertEqual(add_user.status_code, 201)
    
    def test_get_all_users(self):
        response = self.app.get('/api/v1/users')
        self.assertEqual(response.status_code, 200)        
    
