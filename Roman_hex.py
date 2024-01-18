def roman2integer(num):
    dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

    res=0
    pre_val=0
    for symbol in num[::-1]:
         value=dict[symbol]
         if(value>=pre_val):
               res=res+value
         else:
               res=res-value
         pre_val=value
    return res

num=input("Enter a Roman numeral:") 
result=roman2integer(num)
print("Integer value:", result)
