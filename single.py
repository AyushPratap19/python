class Animal:
    def __init__(self, name, species):
        self. name =   name
        self. species = species

    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name,species="Dog" )#to use parent class method we use super().__init__
        self.breed = breed
    def make_sound(self):
        print ( "Bark!")        

d1=Dog("Charlie","Street Dog")  
d1.make_sound()

a1=Animal("Dog","Bull Dog")
a1.make_sound()