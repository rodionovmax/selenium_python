import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class SearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #create a new Firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        #navigate to application home page
        cls.driver.get("http://demo.magentocommerce.com/")
        cls.driver.title

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
        search_field_icon = driver.find_element_by_css_selector(".fa-search")
        search_field_icon.click()
        search_field = driver.find_element_by_css_selector(".search-query")
        search_field.clear()
        search_field.send_keys("camry")
        search_field.submit()
        message = driver.find_element_by_css_selector(".span9 > h2:nth-child(1)")
        print (message.text)
        self.assertEqual("YOUR SEARCH YIELDED NO RESULTS", message.text)

    def test_search_car(self):
        driver = self.driver
        search_field_icon = driver.find_element_by_class_name("fa.fa-search")
        search_field_icon.click()
        search_field = driver.find_element_by_class_name("search-query.form-text")
        search_field.clear()
        search_field.send_keys("car")
        search_button = driver.find_element_by_class_name("mage-btn.btn.btn-default")
        search_button.click()
        products = driver.find_elements_by_class_name("result-title")
        print("Found ", str(len(products)), " products:")
        for product in products:
            print(product.text)
        self.assertEqual(10, len(products))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
        unittest.main()
