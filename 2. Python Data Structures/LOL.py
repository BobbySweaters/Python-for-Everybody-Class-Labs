
name = input('Enter file: ') #Step 1: create a prompt for input wether it be manual text or a file
handle = open(name) #Step 2:  Open the file

counts = dict() #Step 3: Now we create an empty dictionary(historgam pattern)
for line in handle: #Step 4: This line variable is going to iterate once through every line in the dictionary
    words = line.split() #Step 5: split function takes the words and converts them into a list
    for word in words: #Step 6 we create an inner for loop that goes through each of the words we created
        counts[word] = counts.get(word,0) + 1 #Step 7 this makes the hostgram counting the words.

        #* As of now, we have a complete historgram of every word within every line of the file.
    
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print('The word that shows up the most is:',bigword,'It shows up ', bigcount, 'times') 