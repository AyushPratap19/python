def factorial(x):
      if(x==0 or x==1):
        return 1  
      else:
          return factorial(x-1)*x
print(__name__)     #this gives output as __main__ as this is the main file and we are directing running this.
#if you run import2.py then output will be import2    
if __name__=="__main__":     
    print("this is acting as a main function and the execution is stating from here")
    x=int(input("Enter the no. to calculate the factorial"))
    result=factorial(x)
    print(result)

ayush="factorial is calculated"