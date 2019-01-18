from flask import json
from unittest import TestCase
from app import views
from instance import myapp


class ApiTest(TestCase):

    def setUp(self):
        self.app = myapp.test_client()

    def test_registration(self):
        res = self.app.post('/api/v1/users', content_type='application/json',
                            data=json.dumps(dict(firstname="hakeem",
                                                 lastname="matovu",
                                                 email="hakeem@gmail.com",
                                                 phonenumber="0781508582",
                                                 username="hakeem66",
                                                 othername="salim")))

        self.assertEqual(res.status_code, 201)

    def test_get_all_users(self):
        res = self.app.get('/api/v1/users')
        self.assertEqual(res.status_code, 200)

    def test_create_redflag(self):
        res = self.app.post('/api/v1/red_flags',
                            content_type='application/json',
                            data=json.dumps(dict(createdBy="2",
                                                 location="23.444,44,3",
                                                 comment="Missing Funds",
                                                 images="[bridge.jpg]",
                                                 videos="[video1.mp4]"
                                                 )))

        self.assertEqual(res.status_code, 201)

    def test_get_all_redflag_records(self):
        res = self.app.get('/api/v1/red_flags')
        self.assertEqual(res.status_code, 200)

    def test_get_specific_redflag(self):
        res = self.app.get('api/v1/red_flags/1')
        self.assertEqual(res.status_code, 200)

    def test_update_red_flag_location(self):
        res = self.app.patch('api/v1/red_flags/1/location',
                             content_type='application/json',
                             data=json.dumps(dict(location="123.0, 333.2")))
        self.assertEqual(res.status_code, 200)

    def test_update_red_flag_comment(self):
        res = self.app.patch('api/v1/red_flags/1/comment',
                             content_type='application/json',
                             data=json.dumps(dict(
                              comment="Report Case of Missing Funds")))
        self.assertEqual(res.status_code, 200)
"""
    def test_edit_red_flag_(self):
        res = self.app.put('api/v1/red_flags/1/',
                        content_type='application/json',
                        data=json.dumps(dict(
                            comment="Report Corruption")))
        self.assertEqual(res.status_code, 200)
"""
