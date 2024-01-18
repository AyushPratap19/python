#task:we have to raise error if value is not btw 5-9 or any invalid input, but error should not come if we enter "quit"
a = input( "Enter any value between 5and 9" )
if(a=="quit"):
  print("program is terminated")

elif(int(a)<5 or int(a)>9):
  raise ValueError ("**Value should be between 5 and 9**" )
else:
  print(a)


 