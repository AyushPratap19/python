class emp:
    def __init__(self,name,salary):
       self.name=name 
       self.salary=salary

    @classmethod
    def changeStr(self,string):
        return self(string.split("-")[0],int(string.split("-")[1]))
    #if we dont typecast string to int , the output 22000 will be string , lateron if we want to add some increment to the salary we cannot perform + operation on string and int
    #or
    
    @classmethod
    def changeStr2(self,string):
        name,salary=string.split(",")
        return self(name,int(salary))
     
      
e1=emp("Ayush",12000)
print(e1.name,e1.salary)   
#let say someone has given you data in string format like "Ayush-12000"  
#to deal with this we use class method which can be used as constructor for different format data

string="Singh-22000"  
e2=emp.changeStr(string)
print(e2.name,e2.salary) 

e3=emp.changeStr2("Pratap,30000")
print(e3.name,e3.salary)