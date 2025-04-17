# Open Chrome browser on Google Translate website: https://translate.google.com/
#  Find translation text field (the one you send keys to)
# with 3 different locators and print the WebElement you created.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Initialize the WebDriver
driver = webdriver.Firefox()  # Ensure ChromeDriver is in your PATH.

try:
    # Step 2: Open Google Translate
    driver.get("https://translate.google.com/")
    driver.maximize_window()  # Optional: Maximize the browser window.
    time.sleep(2)  # Allow the page to load completely.

    # Step 3: Locate the translation text field using different locators

    # Locator 1: By XPath
    text_field_xpath = driver.find_element(By.XPATH, '//textarea[@aria-label="Source text"]')
    print("Located using XPath:", text_field_xpath)

    # Locator 2: By CSS Selector
    text_field_css = driver.find_element(By.CSS_SELECTOR, 'textarea[aria-label="Source text"]')
    print("Located using CSS Selector:", text_field_css)

    # Locator 3: By Tag Name
    text_field_tag = driver.find_element(By.TAG_NAME, 'textarea')
    print("Located using Tag Name:", text_field_tag)

finally:
    # Step 4: Close the browser
    time.sleep(2)  # Pause for observation
    driver.quit()
