import unittest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from __builtin__ import classmethod

class HomePageTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.get("https://magento.com/")

    def test_check_header(self):
        driver = self.driver
        #header = driver.find_element_by_class_name("main-headline")
        self.assertTrue(self.is_element_present(By., "main-headline"))

    def test_check_navbar(self):
        self.assertTrue(self.is_element_present())
