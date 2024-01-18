class Animal:
    def __init__(self, name, species):
        self. name = name
        self. species = species 
    def show_details(self):
        print(f"Name: {self.name}" )
        print(f"Species: {self.species}")

class Dog(Animal):
    def __init__(self, name, breed):
         Animal. __init__(self, name,species="Dog" )
         self.breed = breed
  
    def show_details(self):
        Animal. show_details (self)
        print(f"breed: {self.breed}")

class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name,breed="Golden Retriever")
        self.color = color

    def show_details (self):
        Dog. show_details (self)
        print(f"Colour: {self.color}")

o1 = GoldenRetriever ("tommy","Black")  
o1.show_details() 
print() 
o2 = Dog ("tommy","german shephard")  
o2.show_details()