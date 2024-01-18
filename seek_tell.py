with open("seek.txt",'r') as f:
    f.seek(10)  #moves the file pointer to 10th postion
  
    data2=f.read(5) #starts reading the content after the 10th position till 5 characters
    print(data2)
    position=f.tell()
    print(position)
with open("seek.txt",'a') as f:   
    f.write("singh") #append is only from the end
    position=f.tell()
    print(position)
with open("seek.txt",'r') as f:
    print(f.read()) 
with open("seek.txt",'a') as f:       
    f.truncate(26) #file will only have 26 characters
with open("seek.txt",'r') as f:
    print(f.read())    
    position2=f.tell()
    print(position2)

    