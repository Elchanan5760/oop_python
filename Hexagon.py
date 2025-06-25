from Square import Square
from math import sqrt

class Hexagon(Square):
    def area(self):
        return (3 * sqrt(3) * self.side ** 2) /2
    def __str__(self):
        if self.side <= 0:
            return "Side nust be positive"
        return f"Hexagon: sides {self.side} area {self.area()}"

o1 = Hexagon("2.5")
print(str(o1))