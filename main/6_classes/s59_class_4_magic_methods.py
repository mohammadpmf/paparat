from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.distance_to_0_0=sqrt(x**2+y**2)

    def __add__(self, other: 'Point'):
        x=self.x+other.x
        y=self.y+other.y
        return Point(x, y)
    
    def __sub__(self, other: 'Point'):
        x=self.x-other.x
        y=self.y-other.y
        return Point(x, y)
    
    def __mul__(self, other: 'Point'):
        x=self.x*other.x-self.y*other.y
        y=self.x*other.y+self.y*other.x
        return Point(x, y)
    
    def __truediv__(self, other: 'Point'):
        return Point(0, 0)

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __del__(self): # destructor
        del self.x
        del self.y
        del self.distance_to_0_0


p1 = Point(3, 4)
p2 = Point(-3, 4)
p3=p1+p2
print(p3)
p1 = 4
p2 = 3
print(p1+p2)
