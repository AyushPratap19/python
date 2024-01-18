#map
list1=[1,2,3,4,5,6]
print(list(map(lambda x:x*x*x,list1)))

#filter
def algo(x):
    return x>2

print(list(filter(algo,list1)))

#reduce
from functools import reduce
num=[1,2,3,4,5]
binary=[0,1,2,3]
num2=[1,0,0,1]

print(reduce(lambda x,y:x+y,num)) #sum of n natural numbers
print(reduce(lambda x,y:x*y,num)) #factorial of a number
print(reduce(lambda x:x*2**binary,num2))
