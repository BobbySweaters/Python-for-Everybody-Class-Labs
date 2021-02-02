
#class is a reserved word



class PartyAnimal: #this is a template for making partyanimal objects
    x = 0 #each party animal has a bit of data. this is an "attribute" now of all partyanlimals

    def party(self): #each patyanimal object has a bit of code
        self.x = self.x +1 #self represents the instance of the class
        print("So far",self.x)

an = PartyAnimal() #mint me a new partyanimal "object" or "instance" based on the template above

an.party() #tell the object to run the party() code within it
an.party()
an.party()
print("Type",type(an)) #you can check the type
print("Dir", dir(an)) #you can check the methods with dir
print()
#! The dir() tells us what the "capabilities" or "methods" of a class are

x = "Hello there"
print(dir(x))