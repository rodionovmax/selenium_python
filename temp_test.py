import unittest
from selenium import webdriver

class TestBasicFunction(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.get("https://google.com")

    def test(self):
        self.search_google = self.driver.find_element_by_id("lst-ib")
        self.search_google.clear()
        self.search_google.send_keys("phones")
        self.search_google.submit()
        products = self.driver.find_elements_by_class_name("r")
        self.assertEqual(11, str(len(products)))

    def tearDown(self):
        self.driver.quit()    

if __name__ == '__main__':
    unittest.main()
