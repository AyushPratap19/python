#walrus operator is used to assign a value to a variable within an expression 
#using :=
#eg1
print(a:=False)
#eg2
b=[1,2,3,4,5]
while(n:=len(b))>0:#while(len(b)>0) willa also work
    print(b.pop())
#eg3
happy = False
print(happy)
print(happy := True)
#eg4(normal)
foods = list()
while True:
    food = input( "What food do you like?: ")
    if food == "quit":
        break
    foods. append (food)  
print(foods)  
#using walrus 
food2=list()
while(food:=input("what food do you like?: "))!="quit":
    food2. append (food) 
print(food2)    

    