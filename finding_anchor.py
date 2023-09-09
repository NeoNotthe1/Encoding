import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter URL - ")

web_html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(web_html, 'html.parser')

# Retrieving all the anchors tag

tags = soup('a')

for tag in tags:
    print(tag.get('href', None))


