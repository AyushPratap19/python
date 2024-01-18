import time
def while_loop():
    i=0
    while(i<5):
        i=i+1

def for_loop():
    
    for i in range(5):
        i=i+1        

prev=time.time()
while_loop()
print(time.time()-prev)#gives the time taken by while loop

prev2=time.time()
for_loop()
print(time.time()-prev2)#gives the time taken by for loop

print("hello")
time.sleep(1) #waits for 3 sec after printing hello
print("I forgot your name")

t=time.localtime() #this gives unformatted time
print(t)
t2=time.strftime("%y-%m-%d %H:%M:%S",t) #%y or %Y both can be used
#%M is for minute and %m is for month
#%D is itself sufficient to print date in mm/dd/yyyy format 
print(t2)