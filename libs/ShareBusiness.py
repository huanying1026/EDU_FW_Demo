# coding:utf-8
from po.LoginPage import LoginPage

#-------------------------------------------------------------------------------
# 函数/过程名称：login_B
# 函数/过程的目的：登录业务函数
# 假设：无
# 影响：无
# 输入：无
# 返回值：无
# 创建者：廖伟新
# 创建时间：2017/11/19
# 修改者：
# 修改原因：
# 修改时间:
#-------------------------------------------------------------------------------

def login_B(UserName='admin',PassWord='admin'):
    obj = LoginPage()
    obj.open_url()
    obj.set_username(UserName)
    obj.set_password(PassWord)
    obj.click_login_button()
    return obj.dv

if __name__ == "__main__":
    login_B('admin','admin')


