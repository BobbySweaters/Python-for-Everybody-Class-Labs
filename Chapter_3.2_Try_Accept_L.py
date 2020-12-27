# in this exercise we are going to include try/except protecton for traceback errors 
# when inputs are strings

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input!")
    quit()
    
pay = h * r

if h <= 40:
    print(pay)
    
elif h >40:
    print(40*r + (h-40)*1.5*r)
    