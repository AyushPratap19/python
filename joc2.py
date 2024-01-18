# joy of coding day 3
str=input()
n=len(str)
c1,c2,c3,c4=0,0,0,0
for i in range(n):
    if(str[i]==')'):
        c1+=1
    else:
        break
str=str[c1:]    
n=n-c1
for i in range(n-1,-1,-1):
    if str[i]=='(':
        c2+=1
        print(i)
    else:
        break

str=str[:n-c2]
n=n-c2
for i in range(n):
    if(str[i]=='('):
        c3+=1
    else:
        c4+=1
print(abs(c4-c3)+c1+c2)            
