# joy of coding day 3
str=input()
n=len(str)
c1=0
c2=0
c3=0

str2=""
for i in range(n):
    if(str[i]==')'):
            c1+=1
            i+=1
    else:
        break 
 

for j in range(i,n):
    str2+=str[j]
m=len(str2)   
for k in range(m):
    if(str2[k]=='('):
        c2+=1
        
        
    elif(str2[k]==')'):
        c3+=1
        
print(abs(c3-c2)+c1) 

