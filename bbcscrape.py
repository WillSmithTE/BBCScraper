import subprocess
import sys

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

install("requests")
install("beautifulsoup4")

class NewsItem:
	def __init__(self, title, url):
		self.title = title;
		self.url = url;

bbcBaseUrl = 'https://www.bbc.com/'

def makeUrl(partialUrl):
	if (bbcBaseUrl in partialUrl):
		return partialUrl
	else:
		return bbcBaseUrl + partialUrl 

import requests
import urllib.request
import time
from bs4 import BeautifulSoup

response = requests.get(bbcBaseUrl)
homePageSoup = BeautifulSoup(response.text, "html.parser")
rawNewsItems = homePageSoup.find_all("a", class_="media__link")

newsItems = []
for item in rawNewsItems:
	fullUrl = makeUrl(item['href'])
	newsItems.append(NewsItem(item.string.strip(), fullUrl));
choiceExit = 'exit'
continueChoice = ''
choiceIndex = 'notachoice'

while continueChoice != choiceExit:
	for index, item in enumerate(newsItems):
		print(str(index + 1) + ' - ' + item.title)

	while 1:
		try:
			choiceIndex = int(input("Select news item index: "))
			break
		except ValueError:
			print("Enter a number matching a news headline")

	choice = newsItems[choiceIndex - 1]
	itemResponse = requests.get(choice.url)
	itemSoup = BeautifulSoup(itemResponse.text, "html.parser")
	storyBody = itemSoup.find("div", "story-body__inner")
	storyPTags = storyBody.find_all("p")
	for ptag in storyPTags:
		print("\n" + ptag.get_text())
	continueChoice = input("\nPress any key to view headlines again, or type 'exit' to exit: ")

