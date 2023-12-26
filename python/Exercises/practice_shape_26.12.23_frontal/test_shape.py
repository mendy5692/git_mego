from circle_class import Circle
from rectangle_class import Rectangle
from math import pi

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
print(f"\ntest 2:\n"
      f"{circle.display_info()}"
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
print(f"\ntest 4:\n{rectangle.display_info()}"
      f"\n==> need to print: ==>\n"
      f"This shape is colored: {rectangle.color}\t\tits length is: {rectangle.length}\tits width is: {rectangle.width}\tits area is: {rectangle.area()}")


