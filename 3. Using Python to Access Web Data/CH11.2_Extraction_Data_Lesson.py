
# Matching and Extracting Data

# - re.search() returns a True/False depending on whether the string matched the regular expressions
# - if we actually want to match the matching strings to be extracted, we use #! find.all()

import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)
print()

y = re.findall('[AEIOU]',x)
print(y)
print()

#! Waring: Greedy Matching
# - The repeat characters (* and +) push outward in both directions (greedy) to match the largest possible string

import re
x = 'From: Using the : character'
y = re.findall('^F.+:', x) # ^means if starts with, .+ is any character one or more times, : is the last character in match is :
print(y)
print()

#! Non-Greedy Matching
# - Not all regular expressions repeat codes are greedy! If you add a ? character, the + and * chill out a bit...

import re
x = 'From: Using the : character'
y = re.findall('^F.+?:', x) #in this instance the ? is used to produce the shortest string. 
print(y)
print()

#! Fine-tuning String Extraction
# you can refine the match for re.findall() and separately determine which portion of the match is to be
# extracted by using parentheses
# Search for lines that start with From and have an at sign
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@', line):
        print(line)
print()

#here is an example of how we searched text for caharcters using the  "find("") function earlier
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ',atpos)
print(sppos)
host = data[atpos+1 : sppos] #this is a string slice
print(host)
print()
#Then we used the double split pattern to achive the same result with a little more elegance

line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split() #split the line into words with spaces = ['from', 'stephen.marquard@uct.ac.za', Sat]
email = words[1] #this pulls the 1 element of the newly created index = stephen.marquard@uct.ac.za'
pieces = email.split('@') #Then split that element stephen.marquard@uct.ac.za by the @ symbol 
print(pieces[1]) #then we call the 1 element after the @ symbol to print
print()
# Now we use expressions to do the same thing. Uses slightly less code and is more powerful, but is complicated syntax
import re
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('@([^ ]*)', line) # this is a way to look through the string until you find the @symbol
print(y)
print()
#! Now here is a little bit of code that can be used to both pick lines and to extract data

import re #re = REGULAR EXPRESSIONS
hand = open('mbox-short.txt')

numlist = list() #creates a list

for line in hand:
    line = line.rstrip() #stripping out the whitespace
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff)!= 1 : continue #! remember, this means keep going through code if condition is true
    num = float(stuff[0])
    numlist.append(num)
print(numlist)


