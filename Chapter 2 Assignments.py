#Write an expression to have the output say "Hello name, then calcuate Total pay based on hours and rate"

name = input("Enter your name: ")
print("Hello",name)

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
pay = float(hours) * float(rate)
print("Pay:",pay)

#Write a program to convert European elevator floors to US floors
#convert elevator floors

inp = input('European Floor? ')
usf = int(inp) + 1
print('US Floor', usf)
