# to print table of 2
for i in range(5):
    print((i+1)*2,end=" ")
print()    
for i in range(1,6):
    print(i*2,end=" ")
print()    
for i in range(2,11,2):
    print(i,end=" ")
    #range(start:  stop:  step:)  stop is till n-1
print()

# for with else 
for i in range(2,11,2):
    print(i,end=" ")
else:
    print("12")       
# else stmt is only executed when there is no break is for loop or for loop is finished completely    
for i in range(2,11,2):
    print(i,end=" ")
    if(i==6):
        break
else:
    print("12") 