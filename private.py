class emp:
    def __init__(self,name,salary):
        self._name=name  #single underscore is used to make the variable protected,but it has no impact ,as it can be accessed directly
        self.__salary=salary  #by using double underscore the variable name has become private

    def __show(self):  #private method
        print(f"Name of employee is {self._name} and salary is {self.__salary}")    
e1=emp("ayush",1000000)
print(e1._name)       #since name is not private it can be accessed
#print(e1.__salary)        #since salary is private is cannot be accessed outside the class
#e1.__show()             #since method is private is cannot be accessed outside the class

#to access private variables we use 'name mangling'
e1._emp__show() #use _classname between object and method to access private methods
print(e1._emp__salary)
print(e1.__dir__()) #tells all the methods applicable on object e1