class ParentClass:
     def parent_method (self):
       print("This is the parent method.")

class Childclass (ParentClass):
    def parent_method (self):
       print("This is the child class parent method.")
       super().parent_method()#using super() we can call parent class method

    def child_method (self):
      print("This is the child method.")
      super().parent_method()

obj1 = Childclass()
obj1.child_method()
obj1.parent_method()#it will call parent method of Clildclass
#if parent_method is not present in child then it automatically calls parent method of Parentclass
#(comment out Childclass parent_method to see)
