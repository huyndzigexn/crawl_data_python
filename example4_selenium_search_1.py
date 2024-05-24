from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver (Chrome in this case)
driver = webdriver.Chrome()

try:
    # Open GearVN website
    driver.get("https://gearvn.com/")

    # Find the search box and enter the search term
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("laptop")
    search_box.send_keys(Keys.RETURN)

    # Wait until the products appear on the page
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".proloop-name a")))

    # Extract the names and prices of products on the first page
    product_names = driver.find_elements(By.CSS_SELECTOR, ".proloop-name a")
    product_prices = driver.find_elements(By.CSS_SELECTOR, ".proloop-price--highlight")

    for name, price in zip(product_names, product_prices):
        # Check if both the name and price are not empty
        if name.text.strip() and price.text.strip():
            print(f"Product: {name.text} - Price: {price.text}")

finally:
    # Close the browser
    driver.quit()
