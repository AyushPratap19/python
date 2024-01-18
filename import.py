import math
result=math.sqrt(16)
print(result)

# #use of from keyword
from math import sqrt,pi
result=sqrt(25)
print(result,pi)
# # NOTE: to import all the functions of math module we use * wildcard
# #but it is not recommended to use , as it creates confusion and make it harder to understandwhere specific functions and variables are coming from

# # use of as keyword
from math import sqrt as s,pi
result=s(81)
print(print(result)) #this first prints the result, after that value of print() function , which is none


# # use of dir keyword
print(dir(math))#this tells all the functions present in math module

#-----------**************VERY IMPORTANT CONCEPT**************-----------#

#importing functions and variables from different files
import import2
result=import2.factorial(5) #we donot have any print stmt still answer is getting printed ,but the output is 
#wrt to user input not the input we passed as a parameter as execution of import2.py starts from main function, not the user defined function.

#there is a print function in the main function , therefore 6 is output if we give 3 as input,after this gets executed ,our factorial function will run for parameter 5 , and result get stored in result variable.

#to avoid main function of import2.py to run (because we are passing the parameter so we only want the result),we uses an idiom called :- if __name__=="__main__":

#using this idiom, main function of import2.py will run only if we are running import2.py file,else only factorial function will run.
print(" ** ",result,import2.ayush," ** ")

