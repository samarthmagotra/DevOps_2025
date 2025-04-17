# Find a way to disable all extensions using Selenium in
# o Chrome
# o Firefox
# o Internet Explorer.
#  Run browsers without extensions.

#CHROME
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")  # Disable all extensions

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open a webpage
    driver.get("https://example.com")
    print("Chrome launched without extensions.")
finally:
    # Close the browser
    driver.quit()


#FIREFOX
# Configure Firefox options
firefox_options = Options()
firefox_options.set_preference("extensions.enabled", False)  # Disable all extensions
firefox_options.set_preference("extensions.autoDisableScopes", 15)  # Disable extensions globally

# Initialize the Firefox WebDriver
driver = webdriver.Firefox(options=firefox_options)

try:
    # Open a webpage
    driver.get("https://example.com")
    print("Firefox launched without extensions.")
finally:
    # Close the browser
    driver.quit()

#IE
# Configure Internet Explorer options
ie_options = Options()
ie_options.add_additional_option("ie.ensureCleanSession", True)  # Start with a clean session
ie_options.add_argument("-extoff")  # No Add-ons mode

# Initialize the IE WebDriver
driver = webdriver.Ie(options=ie_options)

try:
    # Open a webpage
    driver.get("https://example.com")
    print("Internet Explorer launched without add-ons.")
finally:
    # Close the browser
    driver.quit()
