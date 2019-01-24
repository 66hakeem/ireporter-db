from test.base_test import BaseTest


class Test_user(BaseTest):

    def test_user_signup(self):
        reg = self.signup_user(self.user)
        self.assertEqual(reg.status_code, 200)
    
    def test_login(self):
        res = self.login(self.login_data)
        self.assertEqual(res.status_code, 200)
    
    def test_user_login_with_invalid_inputs(self):
        login_data = {'username': 'opio', 'password': ''}
        res = self.login(login_data)
        self.assertEqual(res.status_code, 400)