import requests
import time
from bs4 import BeautifulSoup
from fp.fp import FreeProxy


# Get initial default proxy
base_proxy = FreeProxy().get()

def get_response(url, proxy):
    try:
        print(f"Trying with proxy: {proxy}")  # Debug: print the current proxy being used
        response = requests.get(url, proxies={"http": proxy, "https": proxy})
        # Check HTTP status code
        if response.status_code == 503:
            time.sleep(5)  # Wait for 5 seconds before retrying
            new_proxy = FreeProxy().get()
            print(f'Call {url} again with new proxy: {new_proxy}')
            return get_response(url, new_proxy)  # Recursively call the function with a new proxy
        elif response.status_code != 200:  # Handle other HTTP status codes
            print(f'Non-200 status code {response.status_code} received. Retrying...')
            time.sleep(5)
            new_proxy = FreeProxy().get()
            return get_response(url, new_proxy)
        return response
    except requests.RequestException as e:
        print(f'Error occurred: {e}')
        return None

def print_title(response):
    if response and response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string if soup.title else "No title found"
        print(f"Title of the page: {title}")
    else:
        print("Failed to get a valid response to print title.")

# Call the get_response function with a specific URL and initial proxy
response = get_response('https://topcv.vn/', base_proxy)
if response:
    print(response.status_code)
    print_title(response)
else:
    print('Failed to get a response.')
