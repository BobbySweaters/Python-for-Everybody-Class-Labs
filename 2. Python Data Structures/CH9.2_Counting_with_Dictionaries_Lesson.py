
#! Dictionary as a set of counters: One common ude of dictionries is counting how often we "see" something


ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)
print()

word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)
print()

# We are effectively computing a histogram, which is a statistical term for a set of counters (or frequencies).
# The for loop traverses the string. Each time through the loop, if the character c is not in the dictionary, 
# we create a new item with key c and the initial value 1 (since we have seen this letter once). 
# If c is already in the dictionary we increment d[c].

counts = dict()
names = ['csev', 'cwen','csev','zqian','cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1 #! Histogram logic using if/then/else
print(counts)
print()

#! Python actually has a built in function for Dictionaries = get. The pattern of checking to see if a key is already
#! in a dictionary and assuming the default value if the key is not there is so common that there is a method
#! called get() that does this for us.

if name in counts: #* See how this produced the same result as above?
    x = counts[name]
else : 
    x = 0

x = counts.get(name,0)

#! So, once again = we can use get() and provide a default value of zero when the key os not yet in the dictionary.

counts = dict()
names = ['csev', 'cwen','csev','zqian','cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)