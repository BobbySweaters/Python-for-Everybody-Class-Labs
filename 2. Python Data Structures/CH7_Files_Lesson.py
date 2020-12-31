
#* https://www.py4e.com/html3/07-files

#! Second Memory:
# In this chapter, we start to work with Secondary Memory (or files). Secondary memory is not erased 
# when the power is turned off. Or in the case of a USB flash drive, the data we write from our 
# programs can be removed from the system and transported to another system.

# We will primarily focus on reading and writing text files such as those we create in a text editor. 
# Later we will see how to work with database files which are binary files, specifically designed to be read 
# and written through database software.

#! Opening files:
#When we want to read or write a file (say on your hard drive), we first must open the file. Opening the file 
# communicates with your operating system, which knows where the data for each file is stored. 
# When you open a file, you are asking the operating system to find the file by name and make sure the file exists. 
# In this example, we open the file mbox.txt, which should be stored in the same folder that you are in when you start Python. 
# You can download this file from www.py4e.com/code3/mbox.txt

#! Handle
#* handle = open(filename, mode). Mode is optional and should be 'r' if we intend to read, 'w' if we intend to write.
print()
fhand = open('mbox.txt')
print(fhand)
print()

#! Reading files

#While the file handle does not contain the data for the file, it is quite easy to construct a for loop to read through and count 
# each of the lines in a file:

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)
print()

fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))
print()
print(inp[:20])
print()

#! Searching through a file:
#* We can put an if statement in our for loop to only print lines that meet som criteria.

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip() #! We add this because often times the output usually has \n at the end of lines embedded, and this will prevent uneccesary spacing in the output. 
    if line.startswith('From:'):
        print(line)
print()

#! Skipping with Continue:

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'): 
        continue #! This is a way to skip the lines we aren't interested in, but this produces the same result as above.
    print(line)

#! Prompt for a file name:
fname = input('Enter the file name: ') #!prompt
try: #! add a traceback because of an erroneous filename input by the user
    fhand = open(fname)
except: 
    print('File cannot be opened:', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:') : 
        count = count + 1 #! This is where we count up the number of lines that start with 'Subject'
print('There were', count, 'subject lines in', fname)
