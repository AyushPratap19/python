def Bin2dec(num):
    i=0
    sum=0
    while(num>0):
            rem=num%10
            sum=sum+rem*(2**i)
            i+=1
            num=num//10
    return sum

def oct2dec(num):
    i=0
    sum=0
    while(num>0):
            rem=num%10
            sum+=rem*(8**i)
            i+=1
            num=num//10
    return sum

def oct2hex(num):
    num=oct2dec(num)
    print("octal to decimal is:",num)
    list=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    hex=" "
    while (num>0):
        hex=list[num%16]+hex
        num=num//16
    return hex
        
num=int(input("Enter the Binary Number"))
print("Binary to Decimal is ",Bin2dec(num))
num=int(input("Enter the octal Number"))
print("Octal to HexaDecimal is ",oct2hex(num))
