import unittest
from selenium import webdriver

class SearchTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.get("http://demo.magentocommerce.com/")

    def test_search_fourth(self):
        self.search_field_icon = self.driver.find_elements_by_class_name("fa.fa-search")
        self.search_field_icon.click()
        self.search_field = self.driver.find_elements_by_class_name("form-search")
        self.search_field.clear()
        self.search_field.send_keys("phones")
        self.search_field.submit()

        products = self.driver.find_elements_by_class_name("result-url")
        print ("Found ", str(len(products)), " products:")

        for product in products:
            print(product.text)

        self.assertEqual(10, len(products))

    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main(verbosity=2)
