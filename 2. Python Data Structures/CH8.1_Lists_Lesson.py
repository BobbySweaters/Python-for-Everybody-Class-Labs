
#! Lists
# A list is a sequence
# Like a string, a list is a sequence of values. In a string, the values are characters; in a list, they can be any type. 
# The values in list are called elements or sometimes items. There are several ways to create a new list; the simplest is 
# to enclose the elements in square brackets (“[" and "]”):

#* [10, 20, 30, 40]
#* ['crunchy frog', 'ram bladder', 'lark vomit']

friends = ['Joseph', 'Glenn', 'Sally'] #Strings are now a list of strings when bracketing elements withing the expression
for friend in friends :
    print('Happy New Year: ', friend)

#we use the same index operator to look inside lists

print(friends[1])

#strings are not mutable but lists are. You can look inside lists and change them. Example:

lotto = [2,14,26,41,63]
print(lotto)
lotto[2] = 28
print(lotto) #26 will change to 28 in the list

greet = 'Hello Bob'
print(len(greet))
print(greet)

# Using the range function:
# 1. The range function returns a list of numbers that range from zero to one less than the parameter
# 2. We can construct an index loop using for an integer iterator

print(range(4))
friends = ['Joseph', 'Glenn', 'Sally']
print(list(range(4)))
print(len(friends))
print(list(range(len(friends))))


