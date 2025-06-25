from math import pi
from Shape import Shape

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return pi * self.radius**2
    def __str__(self):
        return f"Circle: radius {self.radius} area {self.area()}"

o1 = Circle(3)
print(str(o1))