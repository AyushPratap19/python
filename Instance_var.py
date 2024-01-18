class emp:
    companyName="Google" #this is class variable 
    empCount=0
    def __init__(self,name):
       self.emp_name=name  #this is instance variable(we have to give name for every emp)
       self.raise_amt=2.0  #this is class variable (if we are keeping it fixed)
       emp.empCount+=1  #this is proper class varibale as it is associated with class(emp.var_name)
       #we donot write it as self.empCount because for every instance empCount will be 1 as empCount is initialized to 0
    def showinfo(self):
        print(f"the name of {self.empCount} employee is {self.emp_name} and the raise amount in {self.companyName} is {self.raise_amt}") 

emp1=emp("Ayush")
emp1.companyName="Apple"
emp1.showinfo() 
#or this can also be written as
emp.showinfo(emp1)

#instance variable can be changed
emp2=emp("Singh")
emp2.raise_amt=3.0
#here our class variable will act as instance variable because we ar initializing it
emp2.showinfo()   


