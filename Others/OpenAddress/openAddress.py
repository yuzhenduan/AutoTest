"""
测试地址访问
打印对应的title
如果能够打开title，说明网页能够打开
否则，输出到日志不能打开
"""
import datetime
from selenium import webdriver
from time import sleep


class OpenAddress:
    def __init__(self):
        '''
        配置驱动类型
        '''
        self.browser = webdriver.Firefox(executable_path="D:\\work\\pycharm\\driver\\Firefox\\geckodriver64.exe")
        self.browser.maximize_window()

    def openAddress(self,url="http://console-test11.369cloud.com"):
        """
        从打开浏览器后开始统计时间
        """
        time = self.curTime()
        try:
            self.browser.get(url)
            title=self.browser.title
            self.myPrint(time,url,"请求页标题为：{0}".format(title))
        except:
            self.myPrint(time,url,"请求失败！")
        finally:
            self.browser.quit()

    def myPrint(self,startTime,url,title):
        '''
        请求成功后打印请求后的时间(后期输入到日志或者格式话输出为html)
        '''
        postTime=self.curTime()
        print("* "*35)
        print("{0}秒请求{1}".format(startTime,url))
        print("{0}秒请求完成\n{1}\n\n".format(postTime,title))

    def curTime(self):
        currentTime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")
        return currentTime


if __name__=="__main__":
    print("first")
    openAddress=OpenAddress()
    print("second")
    openAddress.openAddress("http://console-test11.369cloud.com")
    print("third")