
#! Concatenating Lists using operations
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)
print([0]*4)
print([1,2,3]*3) # * repeats a lost number of given times
print()

#! lists can be sliced using :

t = [9,41,12,3,74,15] #*remember just like in strings, the second number is up to but not including
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])
print()

#! How to check if something is in a list
# Python provieds two operators that let you check if an item is in a list
# These are logical operators that return True or False

some = [1,9,21,10,16]
print(9 in some)
print(15 in some)
print(20 not in some)

#! List are in Order

friends = ['Joseph' , 'Glenn' , 'Sally']
friends.sort() # output will now alphabetically sort
print(friends)
print(friends[1])
print()

#! Built in functions and lists
num = [3,41,12,9,74,15]
print(len(num))
print(max(num))
print(min(num))
print(sum(num))
print(sum(num)/(len(num)))
print()

#! here are some loops to demonstrate calculating average

total = 0
count = 0
while True :
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value =  float(inp)
    total = total + value
    count = count + 1
average = total/count
print('Average: ', average)
print()

#! Now do it using a data structure
numlist = list()
while True :
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value =  float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print('Average using a data structure: ', average)