'''
创建一个跑测试用例的（下面用户已注册）
账户：369CloudTest@datangnet.com.cn
密码：369CloudTest

测试登录：需要用户和密码
默认测试环境为11环境
测试注册：需要用户邮箱和密码和注册码（需要短信验证，不实现，手动测试）
测试环境建议一致，这里驱动路径未开放需要克隆到本地自己调整，要不每次调用需要手动输入该路径

测试分为：
(1)用户名、密码正确
(2)用户名正确、密码不正确
(3)用户名正确、密码为空
(4)用户名不正确、密码正确
(5)用户名、密码不正确
(6)用户名不正确、密码为空
(7)用户名为空、密码正确
(8)用户名为空、密码不正确
(9)用户名、密码为空
'''

import unittest
import os
from selenium import webdriver
from time import sleep


class LoginCase(unittest.TestCase):
    """
    登录测试
    输入地址、用户名和密码
    后期添加手动传username输入框id或classname
    后期添加手动传pwd输入框id或classname
    后期添加手动传submit按钮id或classname
    更高级的延迟实现
    """
    def __init__(self):
        geckodriver="D:\\work\\pycharm\\driver\\Firefox\\geckodriver32.exe"
        isBool=os.path.exists(geckodriver)
        if isBool:
             self.browser=webdriver.Firefox(executable_path=geckodriver)
        else:
             print("{0}不存在！请手动更改为正确路径...".format(geckodriver))
             return
        self.browser.maximize_window()

    def login(self,username="",pwd="",url="http://console-test11.369cloud.com"):
        """
        使用linux逻辑：异常返回1、正常返回0
        需要时，自己可以传递url
        """
        self.browser.get(url)
        self.browser.find_element_by_class_name("form-control").send_keys(username)
        self.browser.find_element_by_class_name("login-input").send_keys(pwd)
        self.browser.find_element_by_class_name("login-button").click()

    def loginFaild(self,username="369CloudTest@datangnet.com.cn",pwd="369CloudTest",message="用户名或密码错误",errClassName="",url="http://console-test11.369cloud.com"):
        self.login(username, pwd,url)
        sleep(3)
        error_message = self.browser.find_element_by_class_name(errClassName).text
        self.assertIn(message, error_message)
        print(message)
        # self.browser.get_screenshot_as_file("localpath")
        # 抓拍快照，暂不实现，后期留传入参数
    #    self.browser.quit()

    def loginSucess(self,username="369CloudTest@datangnet.com.cn",pwd="369CloudTest"):
        # 1.用户名密码正确
        self.login(username, pwd)
        sleep(1)
        link=self.browser.find_element_by_class_name("user-block-name")
        self.assertTrue(username in link.text)
        print(link.text+"登录成功！")
        #self.browser.get_screenshot_as_file("localpath")
        #暂不实现拍摄登录成功图片
       # self.browser.quit()

    def loginPwdError(self,username="369CloudTest@datangnet.com.cn",pwd="buzhengque",errorClassName="alert-danger"):
        # 2.用户名正确、密码不正确
        self.loginFaild(username, pwd,"无效的用户名或密码。",errorClassName)

    def loginPwdNull(self,username="369CloudTest@datangnet.com.cn",pwd="",errorClassName="parsley-custom-error-message"):
        # 3.用户名正确、密码为空
        self.loginFaild(username, pwd, "请输入密码",errorClassName)

    def loginNameError(self,username="buzhengque",pwd="369CloudTest",errorClassName="alert-danger"):
        # 4.用户名不正确，密码正确
        self.loginFaild( username, pwd, "无效的用户名或密码。",errorClassName)

    def loginNamePwdError(self,username="buzhengque",pwd="buzhengque",errorClassName="alert-danger"):
        # 5.用户名、密码不正确
        self.loginFaild(username, pwd, "无效的用户名或密码。",errorClassName)

    def loginNameErrorPwdNull(self, username="buzhengque", pwd="",errorClassName="parsley-custom-error-message"):
        # 6.用户名不正确、密码为空
        self.loginFaild(username, pwd, "请输入密码",errorClassName)

    def loginNameNull(self, username="", pwd="369CloudTest",errorClassName="parsley-custom-error-message"):
        # 7.用户名为空、密码正确
        self.loginFaild(username, pwd, "请输入邮箱",errorClassName)

    def loginNameNullPwdError(self, username="", pwd="buzhengque",errorClassName="parsley-custom-error-message"):
        # 8.用户名为空、密码不正确
        self.loginFaild(username, pwd, "请输入邮箱",errorClassName)

    def loginNameNullPwdNull(self, username="", pwd=""):
        # 9.用户名为空、密码为空
        self.login(username, pwd)
        error_message1 = self.browser.find_element_by_id("parsley-id-4").text
        self.assertIn("请输入邮箱", error_message1)
        error_message2 = self.browser.find_element_by_id("parsley-id-6").text
        self.assertIn("请输入密码", error_message2)
        print(error_message1+"和"+error_message2)
        # self.browser.get_screenshot_as_file("localpath")
        # 抓拍快照，暂不实现，后期留传入参数
    #    self.browser.quit()

if __name__=="__main__":
    print("*"*15+"1.用户名密码正确"+"*"*15)
    login=LoginCase()
    login.browser.delete_all_cookies()
    login.loginSucess("369CloudTest@datangnet.com.cn","369CloudTest")

    print("*"*15+"2.用户名正确、密码不正确"+"*"*15)
    #login = LoginCase()
    login.browser.delete_all_cookies()
    login.loginPwdError("369CloudTest@datangnet.com.cn","buzhengque")

    print("*" * 15 + "3.用户名正确、密码为空" + "*" * 15)
    #login = LoginCase()
    login.browser.delete_all_cookies()
    login.loginPwdNull("369CloudTest@datangnet.com.cn","")

    print("*" * 15 + "4.用户名不正确，密码正确" + "*" * 15)
    #login = LoginCase()
    login.browser.delete_all_cookies()
    login.loginNameError("buzhengque","369CloudTest")

    print("*" * 15 + "5.用户名、密码不正确" + "*" * 15)
    #login = LoginCase()
    login.browser.delete_all_cookies()
    login.loginNamePwdError("buzhengque","buzhengque")

    print("*" * 15 + "6.用户名不正确、密码为空" + "*" * 15)
    #login = LoginCase()
    login.browser.delete_all_cookies()
    login.loginNameErrorPwdNull("buzhengque","")

    print("*" * 15 + "7.用户名为空、密码正确" + "*" * 15)
    #login = LoginCase()
    login.browser.delete_all_cookies()
    login.loginNameNull("","369CloudTest")

    print("*" * 15 + "8.用户名为空、密码不正确" + "*" * 15)
    #login = LoginCase()
    login.browser.delete_all_cookies()
    login.loginNameNullPwdError("","buzhengque")

    print("*" * 15 + "9.用户名为空、密码为空" + "*" * 15)
    #login = LoginCase()
    login.browser.delete_all_cookies()
    login.loginNameNullPwdNull("","")

    login.browser.quit()

    print("Test Sucess!")
#class Register:
#暂不实现