
#! Application 2: Twitter
#* As the Twitter API became increasingly valuable, Twitter went from an open and public API to an API that required the 
#* use of OAuth signatures on each API request.

#* For this next sample program, download the files twurl.py, hidden.py, oauth.py, and twitter1.py from www.py4e.com/code and 
#* put them all in a folder on your computer.

#* To make use of these programs you will need to have a Twitter account, and authorize your Python code as an application, 
#* set up a key, secret, token and token secret. You will edit the file hidden.py and put these four 
#* strings into the appropriate variables in the file:


import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '5'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    print(json.dumps(js, indent=2))

    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])

    for u in js['users']:
        print(u['screen_name'])
        if 'status' not in u:
            print('   * No status found')
            continue
        s = u['status']['text']
        print('  ', s[:50])
