# coding:utf-8

import unittest
from po.LoginPage import LoginPage

class LoginTest(unittest.TestCase):
    '''测试登录功能'''
    def setUp(self):
        self.obj = LoginPage()

    def tearDown(self):
        self.obj.close_broser()

    def test_login_success_001(self):
        '''登录成功验证'''
        self.obj.open_url()
        self.obj.login_operator('admin','admin')
        r = self.obj.get_success_msg()
        self.assertEqual(r, 'admin')

    def test_username_empty_login_002(self):
        '''验证账号为空'''
        self.obj.open_url()
        self.obj.login_operator('','admin')
        r = self.obj.get_username_error_msg()
        self.assertEqual(r,u'帐号或密码不能为空')

    def test_error_login_003(self):
        '''验证正确账号错误密码'''
        self.obj.open_url()
        self.obj.login_operator('admin','123')
        r = self.obj.get_password_error_msg()
        self.assertEqual(r,u'密码错误')


if __name__ == '__main__':
    unittest.main()