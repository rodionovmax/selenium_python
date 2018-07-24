import unittest
from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10)

driver.get("https://github.com/rodionovmax/my_python_projects")

#driver.quit()
