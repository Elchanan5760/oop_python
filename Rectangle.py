
from Shape import Shape


class Rectangle(Shape):
    def __init__(self,height,width):
        self.height = height
        self.width = width
    def area(self):
        return (self.width * self.height)/2
    def __str__(self):
        return f"Rectangle: width {self.width} height {self.height} area {self.area()}"
rect = Rectangle(5,6)
print(str(rect))