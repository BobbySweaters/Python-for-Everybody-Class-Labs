#This is a text file for Chapter 2 examples.

#Get the name of the file an open it
name = input('Enter file:')
handle = open(name, 'r')

#count word frequency (think histogram)
count = dict()
for line in handle:
    words = line.split()
    for words in words:
        count[word] = count.get(word,0) + 1

#find the most common word
bigcount = None
bigword = None
for word, count in counts.items()
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

#all done
print(bigword, bigcount)
