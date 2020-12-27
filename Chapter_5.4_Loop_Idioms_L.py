#Counting in a loop. To add up a variable we encounter in a loop, we introduce a sum variable 
# that starts at 0, and we 1 to it each time through the loop.
zork = 0 #zork is the sum variable
print('Before', zork)
for thing in [9,41,12,3,74,15]:
    zork = zork + 1 #add 1 to the sum variable zork
    print(zork, thing)
print('After', zork)
print()

#Summing in a Loop. To add up a "value" we encounter in a loop, we introduce a sum variable 
# that starts at 0, and we add the "value" to each sum in the loop
zork = 0 #zork is the sum variable
print('Before', zork)
for thing in [9,41,12,3,74,15]:
    zork = zork + thing
    print(zork, thing) # "thing" is the value we defined in the list
print('After', zork)
print()

#Finding the average in a loop. An average just combines the counting and sum patterms
#and divides when the loop is done. 
count = 0
sum = 0
print('Before', count, sum)
for value in [9,41,12,3,74,15] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum/count)
print()

#Filtering in a loop. Filtering is the idea we are looking for something specific in the loop that meets some criteria
#example : is something greater than 20?
print('Before')
for value in [9,41,12,3,74,15] :
    if value >20:
        print('this number', value , 'is Larger than 20')
print('After')
print()

#Search using a boolean variable
#If we just want to search and know if a value was found, we use a variable that 
# starts at False and is set to True as soon as we find what we are looking for.
found = False
print('Before', found)
for value in [9,41,12,3,74,15] :
    if value == 3:
        found = True #we could put a break in here to stop the loop
    print(found, value)
print('After', found)
print()

#finding the smallest value. This is an example where we include the "None" variable. Only one constant (the absence of a value)

smallest = None #this is called a flag value. Picking a number for this really doesn't work well. Use "None" variable
print('Before')
for value in [3,41,12,3,74,15] :
    if smallest is None:
        smallest = value
    elif value < smallest :
        smallest = value
    print (smallest, value)

print('After', smallest)
print()