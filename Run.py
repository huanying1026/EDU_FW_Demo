# coding:utf-8
import time
import copy
import unittest
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from libs.ShareModules import GetSkipScripts
from libs.ShareModules import GetSkipTestCases
from libs.ShareModules import InsertLog
from libs.ShareModules import GetNewReport
from libs.ShareModules import SendEmail

#获取不需要执行的模块名称
ConfigFilePath = "./config.xlsx"
m = GetSkipScripts(ConfigFilePath)

#获取不需要执行的用例名称
TestCasePath = u"./cases/EDU_V1.0测试用例.xlsx"
t = GetSkipTestCases(TestCasePath)

#配置浏览器类型
bs = 'gc'

def create__browser_driver(b=bs):
    try:
        if b == 'gc':
            dv = webdriver.Chrome()
        elif b == 'ff':
            dv = webdriver.Firefox()
        elif b == 'ie':
            dv = webdriver.Ie()
        else:
            pass
        return dv
    except BaseException:
        pass

def get_test_suite(discover):
    #筛选出并去除不需要执行的脚本
    suite_m = copy.deepcopy(discover)
    for i in range(len(m)):
        for j in range(discover._tests.__len__()):
            d = discover._tests[j]
            if m[i] in str(d):
                suite_m._tests.remove(d)
    #筛选出并去除不需要执行的用例
    suite_c = copy.deepcopy(suite_m)
    for i in range(len(t)):
        for j in range(suite_m._tests.__len__()):
            s_m =  suite_m._tests[j]
            for z in range(s_m._tests.__len__()):
                s_c = s_m._tests[z]
                for k in range(s_c._tests.__len__()):
                    s_t = s_c._tests[k]
                    if t[i] == s_t._testMethodName:
                        suite_c._tests[j]._tests[z]._tests.remove(s_t)
    return suite_c

def run_test():
    try:
        dirpath = './scripts'
        discover = unittest.defaultTestLoader.discover(dirpath, pattern='*_tc.py')
        s = get_test_suite(discover)
        currenttime = time.strftime('%y%m%d%H%M%S ')
        filedir = './reports/' + 'report_' + currenttime + '.html'
        fp = open(filedir, 'w')
        runner = HTMLTestRunner(stream=fp,
                                title='Edu自动化测试报告',
                                description='Edu在线教育平台V1.2自动化测试报告',
                                tester="测试大神")
        runner.run(s)
        fp.close()
        # f = GetNewReport()
        # SendEmail('pythondldysl01@163.com','wxqcl258258','2879237501@qq.com','smtp.163.com',f,25)
    except BaseException as msg:
        log = InsertLog()
        log.error(msg)

if __name__ == '__main__':
    run_test()