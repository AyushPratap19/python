fruit="mango"
print(fruit[:5])
# or
print(fruit[0:5]) #starting index:ending index +1
print(fruit[-3:-1])
# LOGIC:- len(fruit)-3:len(fruit)-1
#          [2:4]
print(fruit[-1:-3]) #this will not give an error but will not produce any output becoz[4:2] makes no sense

#jump indexing
print(fruit[0:5:2]) #here jump is of 2 index
print(fruit[::-1])
