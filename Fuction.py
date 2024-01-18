def sum(a,b):
    print('Sum is:',a+b)
def gcd(a,b):    
 pass               #used to maintain Indentation incase we are going to write this function later

x=int(input("enter a number"))
y=int(input("enter a number"))
sum(x,y)
#--------------------------------------------
def multiply(a=5,b=2):  #These are known as default arguments
   print('Product is',a*b)
def multiply2(c,a=5,b=2): #a non default or required argument should be before default arguments
   print('Product2 is',a*b*c)   

x,y,z=2,3,4
multiply(x,y) 
multiply() #if no values are passed then only default arguments are used 
multiply(x) #here a will take the passed value, and b will have its default value
# if we only want to pass value of b then,
multiply(b=4)     #These are known as keyword arguments
multiply2(z)
#--------------------------------------------
# variable length arguments
def average(*number):#  * is used to take many inputs , it it not dereferencing operator
   print(type(number))  #here we get tuple of numbers
   sum=0
   for i in number: 
    sum+=sum+i

   print("Average:",sum/len(number))  

average(2,3)  #we can pass as many values as we want   
#--------------------------------------------
def name( **name ) :# by putting ** the function accesses the arguments by processing them in the form of dictionary.
 print("Hello,", name ["fname" ], name ["mname"], name [ "lname" ])

name(mname = "Pratap", lname = "Singh", fname = "Ayush")
