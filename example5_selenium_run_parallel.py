from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import concurrent.futures
import time

# Function to crawl data from GearVN website
def crawl_gearvn(device):
    driver = webdriver.Chrome()
    try:
        # Open GearVN website
        driver.get("https://gearvn.com/")

        # Find the search box and enter the search term
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(device)
        search_box.send_keys(Keys.RETURN)

        # Wait until the products appear on the page
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".proloop-name a")))

        # Extract names and prices of the products on the first page
        product_names = driver.find_elements(By.CSS_SELECTOR, ".proloop-name a")
        product_prices = driver.find_elements(By.CSS_SELECTOR, ".proloop-price--highlight")

        results = []
        for name, price in zip(product_names, product_prices):
            if name.text.strip() and price.text.strip():
                results.append(f"Product: {name.text} - Price: {price.text}")
        return results

    finally:
        driver.quit()

def main():
    # Using ThreadPoolExecutor to run the crawl_gearvn function in parallel for different devices
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks to the executor for parallel execution
        future_gearvn_laptop = executor.submit(crawl_gearvn, "laptop")
        future_gearvn_mouse = executor.submit(crawl_gearvn, "mouse")

        # Retrieve results from each future
        results_laptop = future_gearvn_laptop.result()
        results_mouse = future_gearvn_mouse.result()

        # Print results for 'laptop'
        print("GearVN Results for 'laptop':")
        for result in results_laptop:
            print(result)

        # Print results for 'mouse'
        print("\nGearVN Results for 'mouse':")
        for result in results_mouse:
            print(result)

if __name__ == "__main__":
    main()



