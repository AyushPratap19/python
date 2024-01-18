rev=input("Enter the Number")
if (rev==rev[::-1]):
    print("The Number is Palindrome", rev)
else:
    print("The Number  is not Palindrome", rev)
for i in set(rev):    
      print(i, "appears", rev.count(str(i)),"times")