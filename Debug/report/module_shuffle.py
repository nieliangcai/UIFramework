import unittest
from selenium import webdriver
class shuffleTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    @unittest.skip
    def tearDown(self):
        self.driver.close()
    def testShuffle(self):
        self.driver.get("http://www.weibo.com")


def suite():
    suite2 = unittest.TestSuite()
    suite2.addTest(shuffleTestCase("testShuffle"))

    return suite2

if __name__=="__main__":
    suite1 = unittest.TestSuite()
    suite1.addTest(shuffleTestCase("testShuffle"))

    runner = unittest.TextTestRunner()
    runner.run(suite1)