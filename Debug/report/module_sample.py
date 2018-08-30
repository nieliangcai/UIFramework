import unittest
from selenium import webdriver
class sampleTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def testSample(self):
        self.driver.get("http://www.baidu.com")


def suite():
    suite1 = unittest.TestSuite()
    suite1.addTest(sampleTestCase("testSample"))

    return suite1

if __name__=="__main__":
    suite1 = unittest.TestSuite()
    suite1.addTest(sampleTestCase("testSample"))

    runner = unittest.TextTestRunner()
    runner.run(suite1)