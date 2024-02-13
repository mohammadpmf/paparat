class Circle:
    pi = 3.14 # class attribute

    def __init__(self, r):
        self.r = r # instance attribute

    def get_perimeter(self):
        return 2*self.r*self.pi
    
    def get_area(self):
        return self.pi*self.r**2


c1 = Circle(15)
c2 = Circle(10)
Circle.pi = 200
print(c1.get_area())
print(c2.get_area())