import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://www.bbc.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
newsItems = soup.find_all("li", class_="media-list__item")
print(newsItems)
