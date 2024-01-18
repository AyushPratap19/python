from dunder import Employee
e1=Employee("Ayush")
print(len(e1))
print(e1) #if we comment out str method than only repr will be printed 
#although we write repr method above str , still it will print str
print(str(e1))
print(repr(e1))
e1()
