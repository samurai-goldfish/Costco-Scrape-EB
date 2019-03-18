# This code actually takes the item and scrapes the price and prints the prices I believe
# based on youtube video:
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup as b

base_url = "https://www.costco.co.uk/Appliances/Small-Kitchen-Appliances/Blenders-Juicers/c/cos_2.5.1"

url = base_url

html = urllib.request.urlopen(url).read()
soup = b(html, "html.parser")

for post in soup.findAll("li", {"class": "product-item vline"}):
	h=link = post.findAll("span", {"class": "notranslate"})[0].text
	print (link)

