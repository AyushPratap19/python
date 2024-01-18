class emp:
    company="Apple"
    def show(self):
        print(f"name of employee is {self.name} and company is {self.company}")
    # @classmethod    
    def changeCompany(self,newCompany): #instead of self , we can use any variable 
        self.company=newCompany
#e1=emp("Ayush")   #if the class has constructor then only we can pass arguments
e1=emp()
e1.name="Ayush"        
e1.show()   
e1.changeCompany("Tesla")
e1.show() 
print(emp.company) #before using ' @classmethod ' it gives Apple , but after using it gives Tesla
#but the variable company has not changed , it is still apple
#to change the value of class variable we use class methods 
