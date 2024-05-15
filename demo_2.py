import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
pageUrl = 'https://en.wikipedia.org/wiki/Main_Page'

# Send a GET request to the URL
r = requests.get(pageUrl)

# Parse the HTML content
soup = BeautifulSoup(r.content, 'html.parser')

# Select all img tags within the specified CSS selector
img = soup.select('#mp-tfp tr td a img')

# Loop through each img tag
for img_tag in img:
    # Get the src attribute of the img tag
    src = img_tag['src']
    # Print the src attribute with the first two characters removed
    print('link img: ' + src[2:])



