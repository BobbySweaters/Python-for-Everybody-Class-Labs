
#! Networked programs
# While many of the examples in this book have focused on reading files and looking for data in those files, there are many 
# different sources of information when one considers the Internet.

# In this chapter we will pretend to be a web browser and retrieve web pages using the Hypertext Transfer Protocol (HTTP). 
# Then we will read through the web page data and parse it.

#Since TCP (and Python) gives us a reliable socket, what do we want to do with socket? What problem do we want to solve>
# Talking to the Web server or mail server, for example. Each have different rules. 

#! Hypertext Transfer Protocol - HTTP
# The network protocol that powers the web is actually quite simple and there is built-in support in Python 
# called socket which makes it very easy to make network connections and retrieve data over those sockets in a Python program

#* Simply said, HTTP protocol is a set of rules to allow browsers to retrieve web documents from servers over the internet. 

#* https://www.w3.org/Protocols/rfc2616/rfc2616.txt

#! An HTTP Request in Python

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode() #this is a prepared request
mysock.send(cmd) #this is the send command to the server

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()