from flask import json
from test.base_test import BaseTest


class Test_interventions(BaseTest):

    """
    def test_get_all_intervention_records(self):
        res = self.app.get('/api/v1/interventions')
        self.assertEqual(res.status_code, 200)
    

    def test_get_specific_intervention(self):
        res = self.app.get('api/v1/intervention/1')
        self.assertEqual(res.status_code, 200)
    
    def test_update_rintervention_location(self):
        res = self.app.patch('api/v1/intervention/1/location',
                             content_type='application/json',
                             data=json.dumps(dict(location="123.0, 333.2")))
        self.assertEqual(res.status_code, 200)
    
    def test_update_intervention_comment(self):
        res = self.app.patch('api/v1/intervention/1/comment',
                             content_type='application/json',
                             data=json.dumps(dict(
                              comment="Report Case of Missing Funds")))
        self.assertEqual(res.status_code, 200)

    """