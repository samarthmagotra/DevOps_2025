# Create a test with the following:
#  Open Google Translate web page
#  Write anything in Hebrew in the text area
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
try:
    driver.get("https://www.translate.google.co.uk")
    driver.maximize_window()
    time.sleep(2)

    text_area = driver.find_element(By.XPATH, '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/div/c-wiz')
    text = "שלום, איך אתה?"
    text_area.send_keys(text)
    time.sleep(2)

    print(f'Entered text is: {text}')

finally:
    time.sleep(2)
    driver.quit()
