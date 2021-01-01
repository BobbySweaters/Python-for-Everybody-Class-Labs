#Here is a more drawn put exaple with explanations to logic

fname = input('Enter File: ') #propt to user
if len(fname) < 1 : fname  = 'clown.txt' #this just allows user to hit enter for text file to auto populate
handle = open (fname) # this opens the input file names fname

di = dict() #dictionary function creates a dictionary
for line in handle: #here is the for loop to iterate what to do for each line of text in the file
    line = line.rstrip() #the strip function precautionarilty takes outany leading or trailing whitespace.
    words = line.split() #If you want to break a string into words into a list, you can use the split method.
    for word in words: #now we create a for loop for the words in the list
        #idiom: retrieve, create, update, counter
        di[word] = di.get(word,0) + 1 #for the list word that we creates, we use the get function to return the value of
        # the item with e specified key

# print(di) - if you want to see the dictionary you created

#! now we want to find the most common word
largest = -1 #we can use -1 because these are counters which will always be positive
theword = None
for k,v in di.items(): #vairables k & v take on assignment for keys and value. items() is a built in function that 
    #enabels us to see the key-value pairs of the dictionary, as tuples in a list. 
    if v > largest :
        largest = v #this is just a max loop essentially looking for the largest number
        theword = k #capture/remember the key that was the largest

print('The word that appears the most is:', theword,)
print('The word',theword,'shows up',largest,'times.')
   
