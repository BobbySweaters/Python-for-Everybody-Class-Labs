#Functions Part 2 Lessons

x = 5
print('Hello')

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day') #You MUST invoke the function

print('Yo')
x = x+2
print(x)

#parameters
def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')

#return statement; 1 - stops 2 - determines the residual value
# Often a function will take it's arguments. do some computation, and return a value to be 
# used as rhe vaue of the function call in the calling expressions. The "return"key word is used for this

def greet():
    return('Hello')

print(greet(), "Glen")
print(greet(), "Sally")      



    