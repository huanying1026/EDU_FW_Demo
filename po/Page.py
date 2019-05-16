# coding:utf-8

from Run import create__browser_driver

edu_url = 'http://localhost/admin.php'

class Page():
    def __init__(self,driver=''):

        b = driver
        if b == '':
            self.dv = create__browser_driver()
        else:
            self.dv = b
        self.dv.maximize_window()
        self.dv.implicitly_wait(10)

    def open_url(self,url=edu_url):
        self.dv.get(url)

    def close_broser(self):
        self.dv.quit()




# from selenium import webdriver
#
# class Page():
#     def __init__(self):
#         self.dv = webdriver.Chrome()
#         self.dv.maximize_window()
#         self.dv.implicitly_wait(10)
#         self.dv.get('http://192.168.1.123/admin.php')
#
#     def close_broswer(self):
#         self.dv.quit()