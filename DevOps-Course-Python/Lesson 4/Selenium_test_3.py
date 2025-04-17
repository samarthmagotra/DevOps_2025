# Open Youtube web page using selenium
#  Type a name of a song
#  Click on search.

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
try:
    driver.get("https://www.youtube.com")
    driver.maximize_window()
    time.sleep(2)

    accept = driver.find_element(By.XPATH,'/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]/ytd-button-renderer[2]')
    accept.click()
    search_bar = driver.find_element(By.NAME, 'search_query')
    song = "Shape of You - Ed Sheeran"
    #search_bar.click()
    search_bar.send_keys(song)
    search_bar.send_keys(Keys.RETURN)
    play = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string')
    play.click()
    time.sleep(3)

    print(f'Song Search complete for: {song}')

finally:
    time.sleep(5)
    driver.quit()
