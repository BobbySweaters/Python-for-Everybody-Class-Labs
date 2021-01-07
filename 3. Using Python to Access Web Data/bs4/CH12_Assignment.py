
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

url = input('Enter - ') #http://py4e-data.dr-chuck.net/comments_1113145.html
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

count_of_spans = 0
sum = 0

spans = soup('span')
for span in spans:
    sum += int(span.contents[0])
    count_of_spans += 1

print('Count ', count_of_spans)
print('Sum ', sum)
print()

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL -') #http://py4e-data.dr-chuck.net/known_by_Zoubaeir.html
repeat = int(input('Enter number of times to repeat: ')) #7
position = int(input('Enter the link position: '))

for i in range(repeat):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    count = 0
    for tag in tags:
        count = count +1
        if count>position:
            break
        url = tag.get('href', None)
        name = tag.contents[0]

print(name)