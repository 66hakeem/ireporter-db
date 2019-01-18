from flask import json
from unittest import TestCase
from app import views
from instance import myapp


class ValidationTest(TestCase):

    def setUp(self):
        self.app = myapp.test_client()

    def test_wrong_firstname_format(self):
        res = self.app.post('/api/v1/users', content_type='application/json',
                            data=json.dumps(dict(firstname="hake em",
                                                 lastname="matovu",
                                                 email="hakeem@gmail.com",
                                                 phonenumber="0781508582",
                                                 username="hakeem66",
                                                 othername="salim")))

        reply = json.loads(res.data)
        self.assertEqual(reply["message"], "wrong first name format")
        self.assertEqual(res.status_code, 400)

    def test_wrong_lastname_format(self):
        res = self.app.post('/api/v1/users', content_type='application/json',
                            data=json.dumps(dict(firstname="hakeem",
                                                 lastname="matovu22",
                                                 email="hakeem@gmail.com",
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
                                                 email="hakeem@gmail.com",
                                                 phonenumber="0781508582we",
                                                 username="hakeem66",
                                                 othername="salim")))

        reply = json.loads(res.data)
        self.assertEqual(reply["message"], "wrong phone number format")
        self.assertEqual(res.status_code, 400)

    def test_wrong_phonenumber_format(self):
        res = self.app.post('/api/v1/users', content_type='application/json',
                            data=json.dumps(dict(firstname="hakeem",
                                                 lastname="matovu",
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
                                                 email="hakeem@gmail.com",
                                                 phonenumber="0781508582",
                                                 username="hakeem66",
                                                 othername="s")))

        reply = json.loads(res.data)
        self.assertEqual(reply["message"], "wrong other name format")
        self.assertEqual(res.status_code, 400)

    def test_spaces_in_email(self):
        res = self.app.post('/api/v1/users', content_type='application/json',
                            data=json.dumps(dict(firstname="hakeem",
                                                 lastname="matovu",
                                                 email="hakeem @gmail.com",
                                                 phonenumber="0781508582",
                                                 username="hakeem66",
                                                 othername="salim")))

        reply = json.loads(res.data)
        self.assertEqual(reply["message"], "Email must not have spaces")
        self.assertEqual(res.status_code, 400)

    def test_wrong_username_format(self):
        res = self.app.post('/api/v1/users', content_type='application/json',
                            data=json.dumps(dict(firstname="hakeem",
                                                 lastname="matovu",
                                                 email="hakeem@gmail.com",
                                                 phonenumber="0781508582",
                                                 username="hake em66",
                                                 othername="salim")))

        reply = json.loads(res.data)
        self.assertEqual(reply["message"], "wrong user name format")
        self.assertEqual(res.status_code, 400)
