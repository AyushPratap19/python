class emp:
    def __init__(self, name):
        self. name = name
    def show(self):
        print(f"the name of emp is {self.name}")    

class dancer:
     def __init__(self, type):
        self. type = type
     def show(self):
        print(f"the name of dance is {self.type}")     

class dancerEmp(emp,dancer):#if we change the order (dancer,emp), then show method of dancer class will be executed
     def __init__(self, name,type):
        self. name = name
        self. type = type

o1=dancerEmp("ayush","kathak")
#print(o1)#can be done only when we have __str__ method
print(o1.name,o1.type)
o1.show()#whichever show method is on the top will get executed
#we have mro function which tells which class methods gets executed in which order
print(dancerEmp.mro())
