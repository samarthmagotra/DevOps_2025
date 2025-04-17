#  Open Firefox browser on any webpage.
#  Delete all cookies from browser.
#  Make sure all cookies are deleted by printing all cookies
# stored in the browser.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Step 1: Initialize the Firefox WebDriver
driver = webdriver.Firefox()  # Ensure GeckoDriver is in your PATH.

try:
    # Step 2: Open any webpage (e.g., example.com)
    driver.get("https://www.example.com")
    print("Opened webpage: https://www.example.com")

    # Step 3: Delete all cookies
    driver.delete_all_cookies()
    print("All cookies deleted.")

    # Step 4: Verify that all cookies are deleted
    cookies = driver.get_cookies()
    print("Remaining cookies:", cookies)  # This should print an empty list

finally:
    # Step 5: Close the browser
    time.sleep(5)
    driver.quit()
