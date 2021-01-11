
#!Retrieving web pages with urllib

# While we can manually send and receive data over HTTP using the socket library, there is a much simpler way to 
# perform this common task in Python by using the urllib library.

# Using urllib, you can treat a web page much like a file. You simply indicate which web page you would 
# like to retrieve and urllib handles all of the HTTP protocol and header details.

# The equivalent code to read the romeo.txt file from the web using urllib is as follows:

import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand: #this for loop will look through each line of data
    print(line.decode().strip()) #line is a bite array, but decode turns it into a string. Strip then separates
    # takes out the extra 
print()

#! As an example, we can write a program to retrieve the data for romeo.txt and compute the 
#! frequency of each word in the file as follows:

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split() #!decode is really the primary difference between using a text file and decoding a URL
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
