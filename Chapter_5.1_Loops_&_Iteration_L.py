#example indefinite loop. Loops (repeated steps) have iterations variables that change each time through a loop.
# Often iteration variables go through a sequence of numbers. "While"loops are the term for infinite loops

n = 5
while n >0:
    print(n)
    n = n-1
print('Blastoff')
print(n)
print()


#finishing an iteration with Continue
#The Continue statement ends the current iteration and jumps to the top of the loop
# and starts the next iteration. "Break" exits the currently executing loop and resumes execution 
# at the next statement

while True:
    line = input('>')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('done')
print()

# definite loops ("for" loops)
for i in [5,4,3,2,1]:
    print(i)
print('Blastoff')

#definite loop with strings

friends = ['Joseph', 'Glen', 'Sally']
for friend in friends :
    print('Happy New Year', friends)
print('Done')

x = 1
while x <= 5:
    print(x)
    x = x+1
print('Done')

#Looking at "in" keyword below. 
# The iteration variable "iterates" through the sequence. In this example, i is the iteration vairable


for i in [5,4,3,2,1]:
    print(i)
print('Blastoff')

