# 1. Write a script which will open the following:
# a. Chrome – http://www.walla.co.il
# b. FireFox – http://www.ynet.co.il

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
#driver2 = webdriver.Chrome()
#driver2.get("http://www.walla.co.il")
driver.get("http://www.python.org")
title = driver.title
assert "Python.org" in driver.title
elem = driver.find_element(By.NAME, "description")
print(title, elem)
driver.quit()






