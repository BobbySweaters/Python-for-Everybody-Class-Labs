
# This task of searching and extracting is so common that Python has a very powerful library called regular expressions 
# that handles many of these tasks quite elegantly. The reason we have not introduced regular expressions earlier 
# in the book is because while they are very powerful, they are a little complicated and their syntax takes some getting 
# used to.

# Regular expressions are almost their own little programming language for searching and parsing strings. 
# As a matter of fact, entire books have been written on the topic of regular expressions. In this chapter, we will only 
# cover the basics of regular expressions. For more detail on regular expressions, see:

#* https://en.wikipedia.org/wiki/Regular_expression

#* https://docs.python.org/library/re.html

#! Regular Expression Quick Guide
#! https://www.py4e.com/lectures3/Pythonlearn-11-Regex-Handout.txt

# ^        Matches the beginning of a line
# $        Matches the end of the line
# .        Matches any character
# \s       Matches whitespace
# \S       Matches any non-whitespace character
# *        Repeats a character zero or more times
# *?       Repeats a character zero or more times 
#        (non-greedy)
# +        Repeats a character one or more times
# +?       Repeats a character one or more times 
#        (non-greedy)
# [aeiou]  Matches a single character in the listed set
# [^XYZ]   Matches a single character not in the listed set
# [a-z0-9] The set of characters can include a range
# (        Indicates where string extraction is to start
# )        Indicates where string extraction is to end

# Search for lines that contain 'From'

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:') >= 0 :
        print(line)

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)

# Search for lines that start with 'From'
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From: '):
        print(line)
print()

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From: ', line): #here we are fine-tuning what is matched by adding special characters to string
        print(line)
print()


# Wild-Card Characters
# The "dot" character matches any character 
# If you add the asterisk character, the character is "any number of times"

# Search for lines that start with 'F', followed by
# 2 characters, followed by 'm:'
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^F..m:', line):
        print(line)