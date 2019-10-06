import unittest
from selenium import webdriver

class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def setUp(self):
        self.driver.get("http://www.so.com")
    def tearDown(self):
        pass

    def test_case01(self):
        input_element=self.driver.find_element_by_id("input")
        input_element.send_keys("肯德基")
        search_botton=self.driver.find_element_by_id("search-button")
        search_botton.click()
        self.assertIn("肯德基" ,self.driver.title)
    def test_case02(self):
        input_element = self.driver.find_element_by_id("input")
        input_element.send_keys("麦当劳")
        search_botton = self.driver.find_element_by_id("search-button")
        search_botton.click()
        self.assertIn("麦当劳", self.driver.title)

if __name__ == '__main__':
    unittest.main()

