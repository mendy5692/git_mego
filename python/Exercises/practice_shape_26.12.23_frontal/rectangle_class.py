from shape_class import Shape


class Rectangle(Shape):
    def __init__(self, color, length, width): #A constructor that inherits the color additionally gets length and width.
        super().__init__(color)
        if length <= 0:
            raise ValueError("length must be pozitive.")
        if width <= 0:
            raise ValueError("width must be pozitive.")
        self.length = length
        self.width = width

    def area(self):                         #A method that calculates the area of a shape
        super().area()
        return self.length * self.width

    def display_info(self):                 #A method that prints the information about the shape.
        return f"{super().display_info()}\t\tits length is: {self.length}\tits width is: {self.width}\tits area is: {self.area()}"
