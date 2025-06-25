from Shape import  Shape

class Square(Shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return  self.side * self.side
    def __str__(self):
        return f"Square: sides {self.side} area {self.area()}"
o1 = Square(2)
print(str(o1))