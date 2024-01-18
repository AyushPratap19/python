ayush=[1,2,3,"pratap",True,56,89]
print(ayush)
print(ayush[3])
print(ayush[::2])
if 56 in ayush:
    print("yes")
else:
    print("no") 

if "pratp" in ayush:
    print("yes")
else:
    print("no")  

if "ay" in "ayush": #can be used in Strings as well
    print("yes")      

#LIST COMPREHSION
lst=[i*i for i in range(5)]
print(lst)   
lst=[i for i in range(5)]
print(lst)
lst=[i*i for i in range(5) if i%2==0]
print(lst)

lst2=["ayush","aarnav","mannu","utkarsh"]
letter_u=[i for i in lst2 if "u" in i]
letter_4=[i for i in lst2 if len(i)>6]
print(letter_u)
print(letter_4)
