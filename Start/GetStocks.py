# import urllib.request
from bs4 import BeautifulSoup
import requests
import time

url = "https://www.google.co.in/finance?q=FB"
print("url -> {}".format(url))

time.sleep(1)
# responseBytes = urllib.request.urlopen(url).read()
# response = responseBytes.decode("UTF-8")
response = requests.get(url).text

soup = BeautifulSoup(response, 'html.parser')
stockPrice = soup.find("meta", {"itemprop": "price"})['content']

print("stock of FB is {}$".format(stockPrice))
