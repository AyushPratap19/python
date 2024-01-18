class MyClass:
    def __init__(self,value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")  

    @property #envoking of getter method
    def modified_value(self):
        return 10*self._value  
    
    @modified_value.setter  #envoking of setter method(it will set the values of modified_value method)
    def modified_value(self,new_value):
        self._value=new_value
            
obj = MyClass(10)
#obj.modified_value = 67 #we cannot change or set the value using getter method
print(obj.modified_value) #it will show the modified value from getter method
obj.show()  #it will show value of the variable that we have passed

obj.modified_value=67  #set the value using the setter method
print(obj.modified_value)
obj.show() 