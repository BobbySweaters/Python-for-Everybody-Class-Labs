
#! Dictionaries
# A dictionary is like a list, but more general. In a list, the index positions have to be integers; 
# in a dictionary, the indices can be (almost) any type.
# You can think of a dictionary as a mapping between a set of indices (which are called keys)
# and a set of values. Each key maps to a value. The association of a key and a value is called 
# a key-value pair or sometimes an item.
# As an example, we’ll build a dictionary that maps from English to Spanish words, so the keys and 
# the values are all strings.
# The function dict creates a new dictionary with no items. Because dict is the name of a built-in function, 
# you should avoid using it as a variable name.


eng2sp = dict()
print(eng2sp)
print()

eng2sp['one'] = 'uno'
print(eng2sp)
print()

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)
print()

# Lists index their positions based on the position in the list. Dictionaries are liek bags - no order. 
# So we ndex the things we put in the dictionary with a lookup tag. 

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)

print(purse['candy'])

purse['candy'] = purse['candy'] + 2
print(purse)

#! Dictionaries are like lists expect they use keys instead of numbers to look up values

