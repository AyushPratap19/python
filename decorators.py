def greet(fun):
    def mfun(*args,**kwargs): #mfun is modified function
        print("Good morning")
        fun(*args,**kwargs)  #agrs stores the elements in the form of tuple and kwargs stores the elements in the form of dictionary
        print("Thanks for using this function")
    return mfun    

@greet  #after calling the greet function we have to write the class or function 
#for which we are using the greet function
def hello():#this function will be passed as a parameter in greet function
    print("Hello World")

@greet
def add():
    a,b=5,6
    print(a+b)

def sub():
    a,b=7,8 
    print(b-a)

def mul(a,b):
    print(b*a) #this function takes arguments

        
hello()
add()  
#or we can also write the same thing as
greet(sub)() #if we are writing like this , then don't write greet above the def function
greet(mul)(2,4) #this will give error as our greet function will only take mul as an arguments, and mfun function is not taking any arguments
#to pass argument in mfun , we use args and kwargs.
  