
# 8.4 Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. For each word on each line check to see if the 
# word is already in the list and if not append it to the list. 
# When the program completes, sort and print the resulting words in alphabetical order.


fname = input("Enter file name: ")
fhand = open(fname)
lst = list() #this list function creates a list object
for line in fhand: # for each line iteration in the file do the folllowing:
    word = line.strip() # 1. take out white space
    word = line.split() # 2. split the strings into a list
    for element in word: # for each element in the list do the following:
        if element in lst : #if word is in the list
            continue #continue looping
        else :
            lst.append(element) #otherwise add the word
lst.sort()
print(lst)


    
    
