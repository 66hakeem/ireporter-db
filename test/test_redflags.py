from flask import json
from test.base_test import BaseTest


class Test_redflags(BaseTest):

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

    def test_update_red_flag_status(self):
        res = self.app.patch('api/v1/red_flags/1/status',
                             content_type='application/json',
                             data=json.dumps(dict(
                              status="Resolved")))
        self.assertEqual(res.status_code, 200)