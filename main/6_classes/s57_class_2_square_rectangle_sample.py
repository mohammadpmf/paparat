from turtle import *

class Square():
    def __init__(self, length=50):
        self.length=length

    def get_perimeter(self):
        return f"The perimeter of this {self} is {4*self.length} meters"
    
    def get_area(self):
        return f"The area of this {self} is {self.length**2} square meters"
    
    def __str__(self):
        return "square"
    
    def draw(self):
        for i in range(4):
            fd(self.length)
            lt(90)

class Rectangle():
    def __init__(self, width=50, height=50):
        self.width=width
        self.height=height

    def get_perimeter(self):
        return f"The perimeter of this {self} is {2*(self.width+self.height)} meters"
    
    def get_area(self):
        return f"The area of this {self} is {self.width**self.height} square meters"
    
    def __str__(self):
        return "rectangle"
    
    def draw(self):
        for i in range(2):
            fd(self.width)
            lt(90)
            fd(self.height)
            lt(90)

s1 = Square(100)
s2 = Square(200)
r3 = Rectangle(10,150)
print(s1.get_area())
print(s2.get_area())
print(s1.get_perimeter())
print(s2.get_perimeter())
s2.draw()
r3.draw()
done()