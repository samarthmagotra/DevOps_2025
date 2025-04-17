# Open any browser on "Github" website.
#  https://github.com/
#  Enter “Selenium” keyword in search textfield
#  Press Enter to search (through code - of course).

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Step 1: Initialize the WebDriver
driver = webdriver.Firefox()  # Replace with 'webdriver.Firefox()' if using Firefox.

try:
    # Step 2: Open GitHub website
    driver.get("https://github.com/")
    driver.maximize_window()  # Optional: Maximize the browser window.
    time.sleep(2)  # Allow the page to load.

    # Step 3: Locate the search text field
    search_field = driver.find_element(By.CLASS_NAME, 'flex-1')  # GitHub search box uses 'name="q"' attribute.
    #search_field.click()
    # Step 4: Enter "Selenium" in the search field
    search_field.send_keys("Selenium")

    # Step 5: Press Enter to search
    search_field.send_keys(Keys.RETURN)
    time.sleep(3)  # Wait for the results page to load.

    # Optional: Print confirmation of the search
    print("Search for 'Selenium' completed on GitHub.")

finally:
    # Step 6: Close the browser
    time.sleep(10)  # Pause for observation.
    driver.quit()
