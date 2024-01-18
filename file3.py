fname=input("enter the filename")
infile=open(fname,"r")
line=int(input("enter no. of lines you want to see"))
for x in range(line):
    a=infile.readline()
    print(x+1,":",a)
infile.seek(0)
word=input("enter a word to see its occurances")
cnt=0
for line in infile: 
    b=line.split()
    cnt+=b.count(word)
print("the word",word,"appeared :",cnt,"times")  