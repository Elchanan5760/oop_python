from Shape import  Shape

class Square(Shape):
    def __init__(self,side):
        # if not isinstance(side,(int,float)):
        #     cond = True
        #     for c in side:
        #         if not c.isdigit and c != ".":
        #             cond = False
        # if cond:
        try:
            side = float(side)

        except:
            print("It must be a number")
            exit()
        self.side = side
    def area(self):
        return  self.side * self.side
    def __str__(self):
        if self.side <= 0:
            return "Side must be positive number"
        return f"Square: sides {self.side} area {self.area()}"
# o1 = Square("-2")
# print(str(o1))