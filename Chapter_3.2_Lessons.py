#Multi-way Conditional 

x = 20
if x<2 :
    print('small')
elif x <10 :
    print('Medium')
else :
    print('LARGE')
print('all done')

#This is my try/except solution from the Chapter 3.2 notry.py file

astr = 'Hello Bob'
try:
    istr = int(astr) 
except:
        istr = -1

print('First', istr)

astr = '123'
try: 
    istr = int(astr)
except:
    istr = -1

print('Second', istr)


#Another Sample try/except
rawstr = input('Enter a nuumber: ')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival >0 :
    print('Nice work')
else:
    print('Not a nunber')
