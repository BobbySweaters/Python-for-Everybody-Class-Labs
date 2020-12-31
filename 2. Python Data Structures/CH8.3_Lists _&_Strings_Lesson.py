
#! Best Friends: Strings & lists

abc = 'With three words'
stuff = abc.split() #! this takes a string and converts it to a list. COME BACK AND LOOK AT THIS LINE!!!
print(stuff)
print(len(stuff))
print(stuff[0])
print(stuff)
for w in stuff :
    print(w)
print()

line = 'A lot         of spaces' #!split will treat this as a single space
etc = line.split()
print(etc)
print()

line = 'first;second;third'
thing = line.split()
print(thing)
print(len(thing))
thing = line.split(';') #! This is how you tell split to delimi using a different character other than a space
print(thing)
print(len(thing))
print()

#!this is an example of how to use split when you want to parse data from a file
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words[2])

print()

line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
print(words)
print()

#! The Double Split Pattern
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
email = words[1]
pieces = email.split('@') #! now we are splitting the variable email that we pulled out of the list with the first split
print(pieces[1])
print()