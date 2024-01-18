country=("spain","germany","india")
print(country)
#tuple manipulaton
temp=list(country)  #changed to list , in order to make changes
temp.append("russia")
print(temp)
temp.pop(0)
print(temp)
temp.insert(2,"finland") #at index 2 finland will be added and russia is shifted to index 3
print(temp)
temp[3]="finland"  #here index is not shifted , the value is overwritten
print(temp)
country=tuple(temp) #again changed to tuple

print(country,len(country),country.count("finland"))

tup=(1,2,3,2,1,2,3,21,2,3,2,1,2,3,2,12,1,1)
print(tup.index(1,5,12)) #tells the index at which 1 has occured after slicing of(5,12)

