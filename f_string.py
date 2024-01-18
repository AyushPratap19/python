# in older versions of python we use format for formatting the string 
txt="hey {} I am fine,I live in {}"
print(txt.format("ayush","India"))
print(txt.format("India","ayush")) 
#this will reverse the value, to avoid this we can give index to the {}

txt2="i watch {1} in sports, and my favorite player is {0}"
print(txt2.format("sachin","cricket"))
#--------------------------------------------------------------------
# now new concept called f string is used
country="india"
name="ayush"
print(f"my name is {name},and i live in {country}")

sport="cricket"
player="sachin"
txt3=f"i watch {sport} in sports, and my favorite player is {player}"
print(txt3)

#if we want txt3 to be printed as it is , we put double curly braces
txt3=f"i watch {{sport}} in sports, and my favorite player is {{player}}"
print(txt3)

print(f"{2*3}")
# the answer 6 will be in string datatype

price=49.0999999
txt4=f"only for {price: .2f} dollar!"
print(txt4)