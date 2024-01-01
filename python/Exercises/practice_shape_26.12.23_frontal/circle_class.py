from math import pi
from shape_class import Shape

'''A subclass that inherits from the Sape class'''
class Circle(Shape):

    def __init__(self, color, radius):      #A constructor that inherits color and also gets a radius length.
        super().__init__(color)
        if radius <= 0:
            raise ValueError("radius must be pozitive.")
        self.radius = radius

    def area(self):                         #A method that calculates the area of a shape
        super().area()
        return pi * self.radius ** 2

    def display_info(self):                  #A method that prints the information about the shape.
        return f"{super().display_info()}\t\tits radius is: {self.radius}\tits area is: {self.area()}"
