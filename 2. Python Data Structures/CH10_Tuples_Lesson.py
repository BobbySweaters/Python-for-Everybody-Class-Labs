
#! Tuples ate immutable
# A tuple1 is a sequence of values much like a list. The values stored in a tuple can be any type, 
# and they are indexed by integers. The important difference is that tuples are #*immutable. 
# Tuples are also comparable and hashable so we can sort lists of them and use tuples as key values in 
# Python dictionaries.

# Syntactically, a tuple is a comma-separated list of values:

t = 'a','b','c','d','e'

# because tuples are immutable, they can be stored more densly than lists, 
# so are effectively a programming efficiency

#! Tuples and Assignment
# we can also put a tuple on the left-hand side of an assignment statement
# we can even omit the parenthases
(x, y) = (4, 'fred')
print(y)
print(x)

#! Tuples and dictionaries 
# the items() method in dictionaries returns a list of (key, value) tuples

d = dict()
d['csev'] = 2
d['cwen'] = 4
for k,v, in d.items():
    print(k,v)
    print()

tups = d.items()
print(tups)

#! Tuples are comparable

(0,1,2) < (5,1,2)

#! Sort by values instead of key
# - if we could construct s list of tuples of the for (value,key) we could sort by value
# - we do this with a for loop that creates a list of tuples

c = {'a':10, 'b':1, 'c':22}
print(c)
tmp = list()
for k,v in c.items():
    tmp.append( (v,k) )
print(tmp)
tmp = sorted(tmp,reverse=True)
print(tmp)
print()

fhand = open('romeo.txt')

counts = dict()
for line in fhand: #outerloop
    words = line.split() 
    for word in words: #innerloop
        counts[word] = counts.get(word, 0) +1 # of this point we have the completed histogram

lst = list()
for key, val in counts.items(): #now we extracting the histogram data out of the dictonary we created
    newtup = (val,key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10] : #this looks for top 10, with list slicing. #!not val and key are flipped
    print(key, val) #now you print it in the order you want to see it

#! Using list comprehension we can create a dynamic list with a much shorter code to get the same as above

c = {'a':10, 'b':1, 'c':22}
print( sorted( [ (v,k) for k,v in c.items() ] ) )


days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[1])

x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
y = x.items()
print(y)