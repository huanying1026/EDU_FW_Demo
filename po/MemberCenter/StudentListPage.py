# coding:utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from po.Page import Page

class StudentListPage(Page):
    u"""学生列表页面"""

    #对象层
    btn_menbercenter_loc = (By.LINK_TEXT,u'会员中心')
    lnk_studentlist_loc = (By.LINK_TEXT, u'学生列表')
    iframe_main_loc = (By.ID, 'mainframe')
    btn_addstudent_loc = (By.LINK_TEXT, u'添加学生')
    msg_phone_number_loc = (By.XPATH, ".//*[@id='recordList']/tr[1]/td[2]")
    lnk_logout_loc = (By.XPATH,".//*[@id='header']/p/a[3]")


    #操作层
    def click_menbercenter_button(self):
        self.dv.find_element(*self.btn_menbercenter_loc).click()

    def click_studentlist_link(self):
        self.dv.find_element(*self.lnk_studentlist_loc).click()

    def change_main_frame(self):
        obj = self.dv.find_element(*self.iframe_main_loc)
        WebDriverWait(self.dv,10,0.5).until(EC.frame_to_be_available_and_switch_to_it(obj))

    def change_default_frame(self):
        self.dv.switch_to_default_content()

    def click_addstudent_button(self):
        self.dv.find_element(*self.btn_addstudent_loc).click()

    def get_addstudent_success_msg(self):
        ele = WebDriverWait(self.dv,10,0.5).until(EC.visibility_of_element_located(self.msg_phone_number_loc))
        return ele.text

    def click_logout_button(self):
        self.dv.find_element(*self.lnk_logout_loc).click()

if __name__ == "__main__":
    pass