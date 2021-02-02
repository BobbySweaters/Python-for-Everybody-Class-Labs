

class PartyAnimal: #this is a template for making partyanimal objects
    x = 0 #each party animal has a bit of data. this is an "attribute" now of all partyanlimals
    
    def __init__(self): #this is a specially named methods
        print("I am constructed")
        #the consructor and deconstructor are optional. The constructor is typically
        #used ro set up variables. The destructor is seldom used.

    def party(self): #each patyanimal object has a bit of code
        self.x = self.x +1 #self represents the instance of the class
        print("So far",self.x)

    def __del__(self):
        print('I am decontructed',self.x)

an = PartyAnimal()
an.party() #calling the party method
an.party()
an.party()
an = 42
print('an contains',an)
print()

#!Now we will create many instances of objects within the class

class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, z): #here we create the parameter z
        self.name = z #stick the paramter into the name
        print(z,'constructed')

    def party(self):
        self.x = self.x +1
        print(self.name, "party count", self.x)

s = PartyAnimal("Sally")
s.party()

j = PartyAnimal("Jim")
j.party()
s.party()            


