import unittest
from selenium import webdriver

class SearchTest(unittest.TestCase)
    @classmethod
    def setUpCls(cls):
        cls.driver = webdriver.Firefox()
        driver = cls.driver
        driver.implicitly_wait(30)
        driver.get("http://demo.magentocommerce.com/")
        driver.title

        cls.click_search_field_icon(driver)

        def click_search_field_icon
