dict={37:"ayush",0o2:"aarnav",17:"akshay"} #leading zero in integer is not permitted, so 0o is used for octal integers
print(dict[0o2])

print(dict.get(37)) #this is also used to access value(error free), if key is not there it will give output as none
print(dict.get("ayush"))#inside get() , we give key ,not the value

for key in dict.keys():
    print(dict[key])  #to print values of dictionary
print(dict.keys())    #to print keys of dictionary
print(dict.values())    #to print values of dictionary 
print(dict.items())  #to print key-values of dictionary

# use of fstring in dictionary
for key in dict.keys():
    print(f"The value corresponding to key {key} is {dict[key]}")
print() #for nextline
for key,value in dict.items():
   print(f"The value corresponding to the key {key} is {value}")

#methods of dictionary
dict2={15:"aditya",16:"jamadaar"}  
dict.update({17:"gaandu"}) #to update any particular key-value pair
dict.update(dict2) #to add more items to dict
print(dict) 

#clear() is used to empty a dictionary
dict2.clear()
print(dict2)

#pop() is used to pop an pair by passing a key
dict.pop(16)
print(dict)
#popitem() is used to pop the last pair 
dict.popitem()
print(dict)
#del() is used to delete items or entire dictionary
del dict2
#print(dict2) this will give an error
del dict[17] 
print(dict)