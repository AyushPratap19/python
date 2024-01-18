a = input ("Enter the number: ")
#let say if we give an non integer input, then our program gets terminated
# and print stmts will not be executed,to prevent this we use try except block
print(f"Multiplication table of {a} is: ")
try:
  for i in range(1, 11):
     print(f"{int(a)} X {i} = {int(a)*i}")
# except Exception as e:  #this gives the reason for occurance of error, after this futher lines of the code will get executed
#    print(e)
except:#here only obaove except block will get executed, comment the above except block to run this manual except block
   print("invaid input!") #this is how we can give manual reason  

print( "Some imp lines of code")
print ("End of program")

#there many many types of errors
#eg:value error,index error
b=(input("enter the index"))
try:
   a=[2,3,4]
   b=int(b)
   print(a[b])
except (ValueError,TypeError): #if we give string input or decimal input
    print("this is value error")
except IndexError: #if we give b value >3
   print("this is an index error")


 
      