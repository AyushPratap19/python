import math
class Shape:
    def showArea(self):
        print("The area of the", self.name, "is", self.area, "units")

class Circle(Shape):
    def __init__(self,radius):
        
        self.name = "Circle"
        self.radius = radius
        self.area = math.pi * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.name = "Rectangle"
        self.length = length
        self.breadth = breadth
        self.area = self.length * self.breadth

class Triangle(Shape):
    def __init__(self,base,height):
        self.name = "Triangle"
        self.base = base
        self.height = height
        self.area = self.base * self.height / 2

c1 = Circle(5)
c1.showArea()

r1 = Rectangle(5, 4)
r1.showArea()

t1 = Triangle(3, 4)
t1.showArea()
