from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# URL of the page to scrape
pageUrl = 'https://en.wikipedia.org/wiki/Main_Page'

# Initialize the Chrome WebDriver (make sure you have chromedriver installed)
driver = webdriver.Chrome()

# Open the webpage
driver.get(pageUrl)

# Find the title element
title_element = driver.find_element(By.CSS_SELECTOR, 'div#mp-welcome')

# Extract the text of the title element
title_text = title_element.text

# Print the title text
print("Title:", title_text)
time.sleep(5)

# Close the WebDriver
driver.quit()





