marks = [12, 56, 32, 98, 12, 45, 1, 4]
 # index = 0          #this is without using enumerate function
 # for mark in marks:
 # print(mark)
# if(index == 3):
 #print( "Harry, awesome!")
# index +=1
for index, mark in enumerate(marks,start=1):
    print(index,mark)
    if (index == 3):
        print("Ayush, awesome!")
     