#it has main.py
class Employee:
   def __init__(self, name):
      self. name = name
#in dunder methods we cannt print anything , we can only return
   def __len__(self):
    i=0
    for c in self.name:
        i=i+1
    return i
   def __repr__(self):
      return(f"The name of the employe is {self. name} repr")
   def __str__(self):
      return(f"The name of the employe is {self. name} str")
   def __call__(self):
      print("hello world") #in callable function we use print
   


       