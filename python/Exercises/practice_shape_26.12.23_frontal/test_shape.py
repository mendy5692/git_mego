from circle_class import Circle
from rectangle_class import Rectangle
from math import pi
'''
def border():
    print("---------------------------------------------------")


circle = Circle("blue", 50)
rectangle = Rectangle("red", 50, 50)

border()

# test 1
if circle.area() == pi * circle.radius ** 2:
    print(f"test 1: it's {True}")
else:
    print(f"test 1: it's {False}")

border()

# test 2
if str(circle.display_info()) == str(f"This shape is colored: {circle.color}\t\tits radius is: {circle.radius}\tits area is: {circle.area()}"):
    print(f"test 2: it's {True}")
else:
    print(f"test 2: it's {False}"
          f"\n{circle.display_info()}"
          f"\n==> need to print ==>\n"
          f"This shape is colored: {circle.color}\t\tits radius is: {circle.radius}\tits area is: {circle.area()}\n")

border()

# test 3
if rectangle.area() == rectangle.length * rectangle.width:
    print(f"test 3: it's {True}")
else:
    print(f"test 3: it's {False}")

border()

# test 4
if rectangle.display_info() == f"This shape is colored: {rectangle.color}\t\tits length is: {rectangle.length}\tits width is: {rectangle.width}\tits area is: {rectangle.area()}":
    print(f"test 4: it's {True}")
else:
    print(f"test 4: it's {False}"
          f"\n{rectangle.display_info()}"
          f"\n==> need to print: ==>\n"
          f"This shape is colored: {rectangle.color}\t\tits length is: {rectangle.length}\tits width is: {rectangle.width}\tits area is: {rectangle.area()}")

border()
'''
bob = Circle("red", 23)
print(bob)