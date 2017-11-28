"""
登录成功为所有类的父类

创建一个跑测试用户（下面用户已注册，只用来跑测试用例）
账户：369CloudTest@datangnet.com.cn
密码：369CloudTest
"""

#import unittest
import os
from selenium import webdriver

class LoginSucess():
    browser=[]
    def __init__(self,driver="geckodriver.exe", driverPath = "D:\\work\\pycharm\\driver\\Firefox\\eckodriver.exe"):
        """
        driver和driverPath扩展是为了能够动态的调整浏览器驱动和所使用的浏览器，后期可以抽象更高级类适配多种浏览器
        """
        driverPath=self.getTruePath(driver,driverPath)
        try:
            self.browser=webdriver.Firefox(executable_path=driverPath)
            #不兼容可能卡死，这里不再向后执行
        except:
            print("geckodriver与浏览器不兼容！")
        self.browser.maximize_window()

    def login(self, username="369CloudTest@datangnet.com.cn", pwd="369CloudTest", url="http://console-test11.369cloud.com"):
        """
        默认在测试环境运行
        """
        self.browser.get(url)
        self.browser.find_element_by_class_name("form-control").send_keys(username)
        self.browser.find_element_by_class_name("login-input").send_keys(pwd)
        self.browser.find_element_by_class_name("login-button").click()

    def getTruePath(self,driver,driverPath=""):
        """
        后期可以把该功能提出去到功能类里面
        """
        isBool=os.path.exists(driverPath)
        driverName=os.path.basename(driverPath)
        if isBool and driver==driverName:
           return driverPath
        else:
            while True:
                print(r"输入格式：D:\\work\\pycharm\\driver\\Firefox\\geckodriver.exe")
                path=input("请输入geckodriver.exe的绝对路径：")
                isBool=os.path.exists(path)
                driverName = os.path.basename(path)
                if isBool and driver==driverName:
                    return path
                else:
                    print("本地不存在或不是指定的驱动，请重新输入！".format(path))

if __name__=="__main__":
    loginSucess=LoginSucess()
    loginSucess.login("369CloudTest@datangnet.com.cn","369CloudTest","http://console-test11.369cloud.com")