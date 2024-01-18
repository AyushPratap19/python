print("hello world")
# or 
print('hello world')
print('hello',7,7+3) #multiple things can be done in single print stmt
# _______________________ 

# ESCAPE SEQUENCE CHARACTERS
# print('hello
#       world') this gives error
print('hello\nworld')
print("hello",7,9,sep='~') #default seprator is space
print("Name   Age",end='::') #default is \n,that's why we dont give \n in python beacoz by default the next print stmt executes from new line
print("Ayush   20")
# _______________________ 
# Operators
print(15//6,15/6) #floor division,normal division
print(3**2) #power
# _______________________ 
# Type casting
# IMPLICIT
a=2
b=2.3
c=a+b #here c is implicitly converted to float,to prevent data loss
print(c)
# EXPLICIT
a=2
b='3'
print(a+int(b))
# _______________________ 
# initializing many variables in single line
c,d,e="apple","mango",'orange'
# if c,d,e="apple":- this doesnt mean apple will eb assigned to all 3 variables
print(c ,'\n', d ,'\n', e) #escape sequence characters dhould be in '' or ""


 
