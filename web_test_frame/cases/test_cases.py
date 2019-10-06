'''
    Instrutions:
        1. 引用test_model 中的测试用例，并对用例进行断言；
'''
import unittest
from time import sleep
from model import test_model
from config import user_config

class CaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = test_model.win_browser(user_config.urls['tg'])

    @classmethod
    def tearDownClass(cls):
        sleep(3)
        test_model.browser_quit(cls.browser)


    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_login(self):
        text = test_model.login(self.browser)
        self.assertEqual(text,'法师打疯狂','登录失败')

if __name__ == '__main__':
    unittest.main()



