from math import pi

from shape_class import Shape


class Circle(Shape):

    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        super().area()
        return pi * self.radius ** 2

    def display_info(self):
        return f"{super().display_info()}\t\tits radius is: {self.radius}\tits area is: {self.area()}"
