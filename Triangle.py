from Rectangle import Rectangle

class Triangle(Rectangle):
    def area(self):
        return (self.height * self.width) /2
    def __str__(self):
        return f"Triangle: width {self.width} height {self.height} area {self.area()}"

o1 = Triangle(3,2)
print(str(o1))