
#! Web Scraping

# Web scraping is when a program or script pretends to be a browser and retirieves web pages, 
# looks at those web pages, extracts information, and then looks at more web pages. 

# search engines scrape web pages - we call this "spidering the web" pr "web crawling"

#! Why scrape?
#! 1. to pull data - particularly social data - who links to who?
#! 2. Get your own data back out of some system that has no export capability
#! 3. monitor a site for new information
#! 4. spider the web to make a databse for a search engine


import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
fhand = open('cover3.jpg', 'wb')
fhand.write(img)
fhand.close()

import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg', 'wb')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    size = size + len(info)
    fhand.write(info)

print(size, 'characters copied.')
fhand.close()


#! Parsing using beautiful soup
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

url = input('Enter - ') #http://www.dr-chuck.com/page1.htm
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser") #soup is the name of the object we created

# Retrieve all of the anchor tags
tags = soup('a') #here we are telling soup to look at our tags
for tag in tags: #here we write a loop to tell it to pull out theurllink
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
