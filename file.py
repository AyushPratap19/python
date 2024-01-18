f = open( 'file2.txt', 'r')
i=0
while True:
    line = f.readline()
    if not line:  #if we write these 2 lines(5,6) at last,then it will show index out of bound error,becoz after printing 3rd time,it will again try to print as the condition is at last
        break
    i+=1
    
    m1 = int(line.split(",")[0]) #first line will splited into 3 parts(because we are spliting when a ,(comma) comes,
    #0th index marks will be assigned to m1 and so on
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    #but these marks are not integers , they are strings
    #if we do {m1*2} then result will be 5252,to get 104, we need to typecast it to int
    #m3 = int(line.split(",")[2]) like this we can type cast it

    print(f"Marks of student {i} in maths is: {m1*2}")
    print(f"Marks of student {i} in english is: {m2}")
    print(f"Marks of student {i} in hindi is: {m3}")

    

