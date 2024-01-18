def fun():
    x=input("enter the number to check odd or even")
    try:
       x=int(x)
       if(x%2==0):
          return 1
       else:
          return 0  
    except:
       print("invalid input")
    finally:
        print("thanks for using this program")
        #The finally block is executed irrespective of the outcome of try…...except....else blocks.One of the important use cases of finally block in a function which returns a value

    
a=fun() 
if(a==1):
    print("even")
else:
    print("odd")       