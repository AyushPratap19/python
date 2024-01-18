def apply(fx, value):  #higher order function
    return 6 + fx(value)

double = lambda x: x * 2
cube = lambda x: x * x * x
avg = lambda x, y, z: (x + y + z) / 3

print( double(5))
print( cube(5))
print( avg(3, 5, 10))
print( apply(lambda x: x * x + x , 2)) #passing lambda function as an argument, here we have passed anonymous function which is not been assigned to any variable
print(apply(cube,5))