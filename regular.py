import re
# [] Represent a character class
# ^ Matches the beginning
# $  Matches the end
# . Matches any character except newline
# ? Matches zero or one occurrence.
# | Means OR (Matches with any of the characters separated by it.)
# * Any number of occurrences(including 0 occurrences)
# + One or more occurrences
# {} Indicate number of occurrences of a preceding
#r"" means raw string
pattern=r"[A-Z]+yclone" 
text='''
tropical Cyclone Dyclone ABcylone Acylonecylone on 7 March
'''
match=re.findall(pattern,text)
print(match)