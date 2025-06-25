
from Shape import Shape


class Rectangle(Shape):
    def __init__(self,height,width):
        try:
            height = float(height)
            width = float(width)
        except:
            print("It must be a number")
            exit()
        self.height = height
        self.width = width
    def area(self):
        return self.width * self.height
    def __str__(self):
        if self.height <= 0 or self.width <= 0:
            return "it must be positive number"
        return f"Rectangle: width {self.width} height {self.height} area {self.area()}"
# rect = Rectangle("-4",6)
# print(str(rect))