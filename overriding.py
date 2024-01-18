class Shape:
    def __init__(self,l,b) -> None:
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b    

class Circle(Shape):
        def __init__(self,r) -> None:
            self.r=r
            super().__init__(r,r) #overriding
        def area(self):
             return 3.14*super().area() 

sq=Shape(2,5)
print(sq.area())        

c=Circle(5)
print(c.area())           
