class person:
    def __init__(self,n,occ):# this is a constructor,this is called automatically when an object is created
        self.name=n #name is the property of the 'a' object and n is the value of the variable
        self.occ=occ
    def info(self):  #self is a reference to the current object
        print(f"{self.name} is a {self.occ}")
a=person("utkarsh","web developer")  #creating object of the class 
a.info()

