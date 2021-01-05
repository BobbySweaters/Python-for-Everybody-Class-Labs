
# example file x = 7746+12+1929+8827+7+8837+128; sum was 27486

import re #re = REGULAR EXPRESSIONS
hand = open('regex_sum_1113143.txt')

numlist = list() #creates a list

for line in hand:
    line = line.rstrip() #stripping out the whitespace
    stuff = re.findall('[0-9]+', line)
    print(stuff)