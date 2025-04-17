# Open Chrome browser on Facebook website https://www.facebook.com/
#  Login into Facebook (No need to send me credentials).

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Step 1: Initialize the WebDriver
driver = webdriver.Firefox()  # Ensure ChromeDriver is in your PATH.
password = os.getenv('PASSWORD')
try:
    # Step 2: Open Facebook
    driver.get("https://www.facebook.com/")
    driver.maximize_window()  # Optional: Maximize the browser window.
    time.sleep(2)  # Allow the page to load completely.

    # Step 3: Locate the email and password fields
    email_field = driver.find_element(By.ID, 'email')  # Facebook email input
    password_field = driver.find_element(By.ID, 'pass')  # Facebook password input

    # Step 4: Input credentials (replace with your own credentials)
    email_field.send_keys("magotra.samarth@gmail.com")
    password_field.send_keys(password)

    # Step 5: Locate and click the login button
    login_button = driver.find_element(By.NAME, 'login')
    login_button.click()

    # Pause to observe the login
    time.sleep(500)

finally:
    # Step 6: Close the browser
    driver.quit()
