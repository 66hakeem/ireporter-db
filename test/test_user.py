from flask import json
from test.base_test import BaseTest


class Test_user(BaseTest):

    def test_user_signup(self):
        reg = self.signup_user(self.user)
        self.assertEqual(reg.status_code, 201)

    def test_login(self):
        res = self.login(self.login_data)
        self.assertEqual(res.status_code, 200)

    def test_user_login_with_invalid_inputs(self):
        login_data = {'username': 'james', 'password': ''}
        res = self.login(login_data)
        self.assertEqual(res.status_code, 400)
    
    def test_get_all_users(self):
        res = self.app.get('/api/v1/users')
        self.assertEqual(res.status_code, 200)

    def test_wrong_firstname_format(self):
        res = self.app.post('/api/v1/users', content_type='application/json',
                            data=json.dumps(dict(firstname="hake em",
                                                 lastname="matovu",
                                                 email="hakeem@gmail.com",
                                                 password="1234567",
                                                 phonenumber="0781508582",
                                                 username="hakeem66",
                                                 othername="salim")))
        reply = json.loads(res.data)
        self.assertEqual(reply["message"], "wrong first name format")
        self.assertEqual(res.status_code, 400)

    def test_missingfields_signup(self):
        res = self.app.post('/api/v1/users', content_type='application/json',
                            data=json.dumps(dict(firstname="hakeem",
                                                 lastname="matovu",
                                                 email="hakeem@gmail.com",
                                                 phonenumber="0781508582",
                                                 username="hakeem66",
                                                 othername="salim")))
        reply = json.loads(res.data)
        self.assertEqual(reply["message"], "some fields are missing")
        self.assertEqual(res.status_code, 400)
    
    def test_wrong_lastname_format(self):
        res = self.app.post('/api/v1/users', content_type='application/json',
                            data=json.dumps(dict(firstname="hakeem",
                                                 lastname="matovu22",
                                                 email="hakeem@gmail.com",
                                                 password="1234567",
                                                 phonenumber="0781508582",
                                                 username="hakeem66",
                                                 othername="salim")))

        reply = json.loads(res.data)
        self.assertEqual(reply["message"], "wrong last name format")
        self.assertEqual(res.status_code, 400)

    def test_wrong_phonenumber_format(self):
        res = self.app.post('/api/v1/users', content_type='application/json',
                            data=json.dumps(dict(firstname="hakeem",
                                                 lastname="matovu",
                                                 password="1234567",
                                                 email="hakeem@gmail.com",
                                                 phonenumber="0781508582we",
                                                 username="hakeem66",
                                                 othername="salim")))

        reply = json.loads(res.data)
        self.assertEqual(reply["message"], "wrong phone number format")
        self.assertEqual(res.status_code, 400)

    def test_othername_format(self):
        res = self.app.post('/api/v1/users', content_type='application/json',
                            data=json.dumps(dict(firstname="hakeem",
                                                 lastname="matovu",
                                                 password="1234567",
                                                 email="hakeem@gmail.com",
                                                 phonenumber="0781508582",
                                                 username="hakeem66",
                                                 othername="s")))

        reply = json.loads(res.data)
        self.assertEqual(reply["message"], "wrong other name format")
        self.assertEqual(res.status_code, 400)

    def wrong_email_format(self):
        res = self.app.post('/api/v1/users', content_type='application/json',
                            data=json.dumps(dict(firstname="hakeem",
                                                 lastname="matovu",
                                                 password="1234567",
                                                 email="hakeemgmail.com",
                                                 phonenumber="0781508582",
                                                 username="hakeem66",
                                                 othername="salim")))

        reply = json.loads(res.data)
        self.assertEqual(reply["message"], "Incorrect email format")
        self.assertEqual(res.status_code, 400)

    def test_wrong_username_format(self):
        res = self.app.post('/api/v1/users', content_type='application/json',
                            data=json.dumps(dict(firstname="hakeem",
                                                 lastname="matovu",
                                                 password="1234567",
                                                 email="hakeem@gmail.com",
                                                 phonenumber="0781508582",
                                                 username="hake em66",
                                                 othername="salim")))

        reply = json.loads(res.data)
        self.assertEqual(reply["message"], "wrong user name format")
        self.assertEqual(res.status_code, 400)