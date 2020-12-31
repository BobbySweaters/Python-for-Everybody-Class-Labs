
#! Counting pattern

counts = dict() # 1. make a dictionary
print('Enter a line of text: ') #2. Read a line of text
line = input('') #line of text goes into this variable line

words = line.split() #then we split it

print('Words: ', words) # now we going to print those words out that the user input to get a list of words in dictionary form

print('Counting...')
for word in words: # now we write the loop to count the words in a histogram fashion with get function
    counts[word] = counts.get(word,0) + 1
print('Counts' , counts)
print()

#! Using a for loop to go through a dictionary. Eve though dictionaries are not stored in order we write a for loop
#! that goes through all of the entries in a dictioary - actually goes through all keys in the dictionary and 
#! looks up the values.

counts = {'chuck': 1, 'fred': 42, 'jan' : 100}
for key in counts:
    print(key, counts[key])

#! Retrieving lists of Keys & values
jjj = {'chuck': 1, 'fred': 42, 'jan' : 100}
print(list(jjj))
print(jjj.values())
print(jjj.items()) #items gives us back a list of key items pairs
print()

#! Bonus: Two iteration variables!!
# we can loop through the key value pairs in a dictionary using two iteration variables. The first 
# variable is the key and the second variable is the corresponding value for key

jjj = {'chuck': 1, 'fred': 42, 'jan' : 100}
for aaa,bbb in jjj.items() :
    print(aaa,bbb)

#! now we can circle back and bring this all together

name = input('Enter file: ') #Step 1: create a prompt for input wether it be manual text or a file
handle = open(name) #Step 2:  Open the file

counts = dict() #Step 3: Now we create an empty dictionary(historgam pattern)
for line in handle: #Step 4: This line variable is going to iterate once through every line in the dictionary
    words = line.split() #Step 5: split function takes the words and converts them into a list
    for words in words: #Step 6 we create an inner for loop that goes through each of the words we created
        counts[word] = counts.get(word,0) + 1 #Step 7 this makes the hostgram counting the words.

        #* As of now, we have a complete historgram of every word within every line of the file.
    
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount) 