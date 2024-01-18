x=[1,2,3]
print(dir(x))
#dir retruns all the methods and attributes available for an object

class Person:
   def __init__(self, name, age):
      self.name=name
      self. age = age

p = Person( "John", 30)
print(p.__dict__)
#__dict__ is an attribute which returns a dictionary representation of an object's attributes.
#useful in introspection


print(help(Person))
#help() functions gives all information about an object