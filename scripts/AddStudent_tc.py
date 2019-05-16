# coding:utf-8
import unittest
import sys
sys.path.append('../')

from libs.ShareBusiness import login_B
from libs.ShareModules import InsertLog
from po.MemberCenter.StudentListPage import StudentListPage
from po.MemberCenter.StudentList.AddStudentPage import AddStudentPage


class AddStudentTest(unittest.TestCase):
    u'''添加学生功能测试'''
    def setUp(self):
        self.b = login_B()
        self.obj_sp = StudentListPage(self.b)
        self.obj_ap = AddStudentPage(self.b)
    def tearDown(self):
        self.obj_ap.close_broser()


    def addstudent_verify(self,username,realname,password,sex,role,category,email,phone):
        try:
            self.obj_sp.click_menbercenter_button()
            self.obj_sp.click_studentlist_link()
            self.obj_sp.change_main_frame()
            self.obj_sp.click_addstudent_button()
            self.obj_ap.set_username_input(username)
            self.obj_ap.set_realname_input(realname)
            self.obj_ap.set_password_input(password)
            self.obj_ap.select_sex_radio(sex)
            self.obj_ap.select_role_select(role)
            self.obj_ap.select_start_student_input()
            self.obj_ap.upload_head_portrait()
            self.obj_ap.select_category_select(category)
            self.obj_ap.set_email_input(email)
            self.obj_ap.set_phone_input(phone)
            self.obj_ap.click_save_button()
            self.obj_ap.click_alert_confirm_button()
            self.obj_ap.click_comeback_button()
            msg = self.obj_sp.get_addstudent_success_msg()
            return msg
        except BaseException as msg:
            log = InsertLog()
            log.error(msg)

    def test_addstudent_success(self):
         u'''成功添加学生账号测试'''
         msg = self.addstudent_verify('13811112222','test007','123456',1,u'全部开放',u'南通大学','xiaoxin@163.com','13811112222')
         self.assertEqual(msg,'13811112222')

if __name__ == '__main__':
    unittest.main(verbosity=2)



