import unittest
from selenium import webdriver

class SearchTests(unittest.TestCase)
    def setUp(self):
        #create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)

        #navigate to google.com
        self.driver.get("https://google.com")

    def test_search(self):
        self.search_google = self.driver.find_element_by_id("lst-ib")
        self.search_google.clear()
        self.search_google.send_keys("phones")
        self.search_google.submit()

        products = self.driver.find_elements_by_class_name("")
