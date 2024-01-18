class math:
    def __init__(self,num):
        self.num=num
    def add(self,num2): #instance method
        self.num+=num2
    @staticmethod   #declaration 
    def add2(a,b):
        return a+b

print(math.add2(1,2)) #no need to create object to use a static method 
a=math(5)
a.add(2)
print(a.num) # for instance method we need to create an object
