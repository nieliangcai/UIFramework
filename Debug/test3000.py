from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import unittest
import time,os
from Debug import login_page,test_page
from utils.HTMLTestRunner_PY3 import HTMLTestRunner
from selenium.webdriver.common.action_chains import ActionChains

class testcase(unittest.TestCase):
    url = "http://118.31.19.120:3000/"
    login_loc = (By.XPATH,'//*[text()="登录"]')       #获取2个登录

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url=self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


    @classmethod
    def tearDownClass(self):
        pass
        # self.driver.close()

    def test_login(self):
        '''先登录'''
        driver = self.driver
        driver.find_element(*self.login_loc).click()
        driver.find_element(*login_page.login_user).send_keys('testuser2')
        driver.find_element(*login_page.login_pwd).send_keys('123456')
        driver.find_element(*login_page.login_pwd).submit()

    def test_topic(self):
        '''发布话题'''
        driver = self.driver
        driver.find_element(*test_page.topic_loc).click()   #点击发布话题按钮
        select  = driver.find_element(*test_page.select_loc)    #选择share
        Select(select).select_by_value('share')
        driver.find_element(*test_page.title_loc).send_keys('这个select框是By_Value')
        print(1)
        # ActionChains(driver).double_click(*test_page.content_loc).perform()
        JS = 'document.getElementsByClassName("CodeMirror-cursor")[0].style.visibility="visible";document.getElementsByTagName("pre")[1].innerText="21312321gsadfgaswqeqsad a"'
        JS2 = 'var data = "xiaoxinzouhuo";document.getElementsByClassName("CodeMirror-scroll")[0].innerHTML ="<pre>"+data+"</pre>"'
        driver.find_element_by_class_name("CodeMirror-scroll").click()
        driver.execute_script(JS2)
        print(4)

        # driver.find_element(*test_page.content_loc).send_keys('51243512736123123781276')
        print(2)
        driver.find_element(*test_page.submit_loc).click()
        print(3)

if __name__=="__main__":
    now = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    report = os.path.join(os.path.dirname(os.path.abspath(__file__)),'report','results_%s.html' %now)
    suite = unittest.TestSuite()
    # suite.addTest(testcase("test_login"))
    # suite.addTest(testcase("test_topic"))
    suite.addTests([testcase("test_login"),testcase("test_topic")])
    with open(report,'wb') as f:
        runner = HTMLTestRunner(f,verbosity=2,
                                title='复习HTMLTestRunner',
                                description='发送一个登录用例报告')
        runner.run(suite)
