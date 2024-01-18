import time
timestamp1 = time. strftime('%H:%M:%S')         
print (timestamp1)
timestamp2 = int(time.strftime('%H'))
print(timestamp2)
timestamp3 = int(time.strftime('%M'))
print(timestamp3)
timestamp4 = int(time.strftime('%S'))
print(timestamp4)

# timestamp1 gives the full time,timestamp2 gives the hour,timestamp3 gives the minute,timestamp4 gives the seconds.


if(timestamp2<=12 and timestamp2>=00):
    print("Good Morning\n")
   
elif(timestamp2>12 and timestamp2<=18):
    print("Good Afternoon\n")
   
else:
    print("Good Evening\n")
       