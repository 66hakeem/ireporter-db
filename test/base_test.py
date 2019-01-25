from unittest import TestCase
from flask import json
from app import views
from app.db import Database
from instance import myapp


class BaseTest(TestCase):

    def setUp(self):
        self.app = myapp.test_client()
        self.user = {
            'firstname': 'hakeem',
            'lastname': 'matovu',
            'email': '66hakeem@gmail.com',
            'password': '1234567',
            'phonenumber': '0704527580',
            'username': 'hakeemcapt',
            'othername': 'salim'
        }
        self.redflag_incident = {
            'location': '234.9, 321.2',
            'comment': 'Stolen Funds',
            'images': 'image.png',
            'videos': 'videos.mp4'
        }
        self.login_data = {
            'username': 'hakeemcapt',
            'password': '1234567'
        }

    def signup_user(self, user):
        user_res = self.app.post('/api/v1/users', content_type='applicat\
                                 ion/json', data=json.dumps(user))
        return user_res

    def login_token(self, userinfo):
        log_res = self.app.post('api/v1/auth/login', content_type='\
                                ation/json', data=json.dumps(userinfo))
        res_data = json.loads(log_res.data.decode())
        token = res_data['token']
        return token

    def login(self, userinfo):
        res = self.app.post('/api/v1/auth/login', content_type='applica\
                            tion/json', data=json.dumps(userinfo))
        return res

