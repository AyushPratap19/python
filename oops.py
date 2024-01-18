class person:
    name="ayush"  #these are default values
    occ="student"
    def info(self):  #self is a reference to the current object
        print(f"{self.name} is a {self.occ}")
a=person()  #creating object of the class 
b=person()
print(a.name)
a.name="mannu"
a.occ="chhhapri"
a.info()
b.info()
