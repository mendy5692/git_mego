'''The base class of some sape'''
class Shape():

    def __init__(self, color):  #A constructor that receives color.
        self.color = color


    def area(self):             #A method that calculates the area of a shape
        pass

    def display_info(self):     #A method that prints the information about the shape.
        return f"This shape is colored: {self.color}"


