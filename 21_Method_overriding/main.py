from math import pi, floor

class Shape:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

    def area(self):
        area = self.x * self.y
        print(f"Area is {area} sq.units")
        return area

    

class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius
        super().__init__(radius,radius)

    def area(self):
        print(pi * super().area())

    # def area(self):
    #     area = floor((pi * (self.radius**2)))
    #     print(f"Area is {area} sq.units")

    
rec = Shape(4,5)
rec.area()

cir = Circle(5)
cir.area()