class Employee:
    def __init__(self, name, id):
        self.name = name
        self. id = id

    def showDetails (self):
        print(f"The name of Employee:{self.id} is {self.name}")

class Programmer (Employee):
    def showLanguage(self):
        print("The default langauge is python")

e1 = Employee( "Ayush", 400)
e1. showDetails()
e2 = Programmer ("Singh", 4100)
e2. showDetails()
e2. showLanguage()