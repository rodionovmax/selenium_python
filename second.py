from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("https://google.com")
search_field = driver.find_element_by_id("lst-ib")
search_field.clear()
search_field.send_keys("phones")
search_field.submit()

products = driver.find_elements_by_class_name("r")
print ("Found ", str(len(products)), " products:")

for product in products:
    print (product.text)

driver.quit()
