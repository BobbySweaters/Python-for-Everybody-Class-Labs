
#Use the file name test.txt as the file name

fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print('File:', fname, 'does not exist. Please check spelling or file location.')
    exit()

count = 0
total = 0
answer = 0

for line in (fhand):
    if line.startswith("A"): 
        count = count + 1
        number = line.find('0')
        number = float(line[number:])
        total = number + total

answer = total / count
print(total)
print('Line Count: ',count)
print('Average spam confidence:mbox-short.txt',answer)