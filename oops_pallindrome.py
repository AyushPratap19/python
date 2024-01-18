class String:

    def check(self, Str):
        if Str == Str[::-1]:
            print("Given string is a Palindrome")
        else:
            print("Given string is not a Palindrome")

class Integer(String):
   
    def check(self, num):
        temp = num
        sum = 0
        while temp != 0:
            rem = temp % 10
            sum = (sum*10) + rem
            temp = temp //10

        if num == sum:
            print("Given integer is a Palindrome")
        else:
            print("Given integer is a not a Palindrome")

str = input("Enter a string : ")
Obj1 = String()
Obj1.check(str)
    

num = int(input("Enter a integer : "))    
Obj2 = Integer()
Obj2.check(num)
