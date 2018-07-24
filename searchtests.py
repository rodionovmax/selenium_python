import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class SearchTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.get("http://demo.magentocommerce.com/")

    def test_search_phones(self):
        driver = self.driver
        search_field_icon = driver.find_element_by_css_selector(".fa-search")
        #search_field_icon.move_to_element(search_field_icon)
        search_field_icon.click()
        time.sleep(3)
        free_demo = driver.find_element_by_css_selector("div.nav-demo > a:nth-child(1)")
        #actions.move_to_element(free_demo)
        ActionChains(self.driver).move_to_element(free_demo).perform()
        time.sleep(3)
        #self.driver.find_element_by_css_selector(".fa-search").move_to_element(".fa-search")
        search_field = driver.find_element_by_css_selector(".search-query")
        search_field.clear()
        search_field.send_keys("phones")
        search_field.submit()

        products = driver.find_elements_by_class_name("result-url")
        print ("Found ", str(len(products)), " products:")

        for product in products:
            print(product.text)

        self.assertEqual(10, len(products))

    def test_search_by_name(self):
        driver = self.driver
        search_field = driver.find_element_by_css_selector(".search-query")
        search_field.clear()
        search_field.send_keys("camry")
        search_field.submit()
        products = driver.find_elements_by_class_name("result-url")
        print ("Found ", str(len(products)), " products:")
        for product in products:
            print(product.text)
        self.assertEqual(10, len(products))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
        unittest.main()
