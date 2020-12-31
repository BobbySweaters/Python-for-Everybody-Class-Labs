
#! 6.1 Strings
#* https://www.py4e.com/html3/06-strings
# A string is a sequence of characters.
# You can access the characters one at a time with the bracket operator:
fruit = 'banana'
letter = fruit[1]
print(letter)
print()

letter = fruit[0]
print(letter)
print()

#  b  a  n  a  n  a
# [0][1][2][3][4][5]
# So “b” is the 0th letter (“zero-th”) of “banana”, “a” is the 1th letter (“one-th”), 
# and “n” is the 2th (“two-th”) letter.

#len is a built-in function that returns the number of characters in a string:
fruit = 'banana'
print("This is one way to print the length of the string: ",len(fruit))
print()
#or
fruit = 'banana'
x = len(fruit)
print('This is an alternative way to print the length of a string: ', x)
print()

#! Traversal through a string with a loop
# A lot of computations involve processing a string one character at a time. 
# Often they start at the beginning, select each character in turn, do something to it, 
# and continue until the end. This pattern of processing is called a traversal. 
# One way to write a traversal is with a while loop:

fruit = 'banana' #same variable from above
index = 0 #this is the iteration variable used in the next line
while index < len(fruit): #the length of fruit is 6. Count the 0 index as 1.
    letter = fruit[index] # The square brackets are used to index elements in strings. Specifically, fruit[index]
    print(index, letter)
    index = index + 1
print()

#! here is proof for line 36 above to demonstrate how fruit is being indexed with position 0
print(fruit[0])
print()

#! For Loops
# A much more convenient way to loop through strings is using a determiniate loop which uses the "for" statement
# In a for loop, the itertion variable is completely taken care of by the for loop. As can be seen below this is much 
# more elegant. 

fruit = 'banana'
index = 0
for letter in fruit:
    print(index, letter)
    index = index +1
print()

#! Looking deeper into "in"
# 1. The iteration variable iterates through the sequence (ordered set)
# 2. The block (body) of code is executed once for each value in the sequence. 
# 3. The iteration variable moves through all of the values in the sequence.

for letter in "banana":
    print(letter)
print()

#!Slicing
# A segment of a string is called a slice. Selecting a slice is similar to selecting a character:

s = "Monty Python"
print(s[0:4])
print(s[6:7])
print(s[6:20]) #note that referencing beyond a string does not cause an error
print()

#! 6.2 Manipulating Strings
# Strings are immutable
# It is tempting to use the operator on the left side of an assignment, with the intention of changing 
# a character in a string. For example:

# >>> greeting = 'Hello, world!'
# >>> greeting[0] = 'J'
# TypeError: 'str' object does not support item assignment

# The reason for the error is that strings are immutable, which means you can’t change an existing string. 
# The best you can do is create a new string that is a variation on the original:

greeting = 'Hello, world!'
new_greeting = 'J' + greeting[1:]
print(new_greeting)
print()

#! String Comparison
# The comparison operators work on strings. To see if two strings are equal:
word = "banana"
if word == 'banana':
    print('All right, bananas.')
print()

new_word = 'apple'
if new_word < 'banana':
    print('Your word, ' + new_word + ', comes before banana.')
elif word > 'banana':
    print('Your word, ' + new_word + ', comes after banana.')
else:
    print('All right, bananas.')
print()

#! String Library
# 1. Python has a number of string functions which are in the string library. These functions are already built
# into every string, we just invoke them by appending the function to the string variable:
greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print()

#! String Methods
# Strings are an example of Python objects. 
# An object contains both data (the actual string itself) and methods, which are effectively 
# functions that are built into the object and are available to any instance of the object.
# Python has a function called dir which lists the methods available for an object. 
# The type function shows the type of an object and the dir function shows the available methods.
stuff = 'Hello world'
dir(stuff)

#* https://docs.python.org/3/library/stdtypes.html#string-methods

#example using find string method:
word = 'banana'
index = word.find('a')
print(index)
print()

##example using replace string method:
greet = 'Hello Bob'
nstr = greet.replace('Bob','Jane')
print(nstr)
print()

#example stripping whitespace
line = '    Hello Bob   '
print(line.strip())
print()

#! Parsing strings
# Often, we want to look into a string and find a substring. 
# For example if we were presented a series of lines formatted as follows:
#* From stephen.marquard@ uct.ac.za Sat Jan  5 09:14:16 2008
# and we wanted to pull out only the second half of the address (i.e., uct.ac.za) from each line, 
# we can do this by using the find method and string slicing.

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ',atpos)
print(sppos)
host = data[atpos+1:sppos]
print(host)
