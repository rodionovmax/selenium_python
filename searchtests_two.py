import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class SearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        #driver = cls.driver
        cls.driver.implicitly_wait(30)
        cls.driver.get("http://demo.magentocommerce.com/")
        cls.driver.title

        #cls.driver.click_search_field_icon(driver)
        cls.driver.find_element_by_css_selector(".fa-search").click()
        #cls.driver.move_to_free_demo(driver)
        ActionChains(cls.driver).move_to_element(cls.driver.find_element_by_css_selector("div.nav-demo > a:nth-child(1)")).perform()

    def test_search_aphones(self):
        driver = self.driver
        self.search_send_keys(driver, keys="phones")
        self.assertion_with_results(driver)
        time.sleep(1)

    def test_search_car(self):
        driver = self.driver
        self.search_send_keys(driver, keys="car")
        self.assertion_with_results(driver)
        time.sleep(1)

    def test_search_by_name(self):
        driver = self.driver
        self.search_send_keys(driver, keys="camry")
        self.assertion_with_no_results(driver)
        time.sleep(1)


    # Subsidiary methods
    def click_search_field_icon(cls, driver):
        driver = cls.driver
        driver.find_element_by_css_selector(".fa-search").click()

    def move_to_free_demo(cls, driver):
        driver = cls.driver
        free_demo = driver.find_element_by_css_selector("div.nav-demo > a:nth-child(1)")
        ActionChains(cls.driver).move_to_element(free_demo).perform()

    def search_send_keys(self, driver, keys):
        driver = self.driver
        search_field = driver.find_element_by_css_selector(".search-query")
        search_field.clear()
        search_field.send_keys(keys)
        search_field.submit()

    def assertion_with_results(self, driver):
        products = self.driver.find_elements_by_class_name("result-title")
        print("Found ", str(len(products)), " products:")
        for product in products:
            print(product.text)
        self.assertEqual(10, len(products))
        #product = None
        #products = None

    def assertion_with_no_results(self, driver):
        message = driver.find_element_by_css_selector(".span9 > h2:nth-child(1)")
        print(message.text)
        self.assertEqual("YOUR SEARCH YIELDED NO RESULTS", message.text)
        del message

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
