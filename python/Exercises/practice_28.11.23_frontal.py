'''
a=b=c=d=e=12
print(a)
print(b)
print(c)
print(d)
print(e)
print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(id(e))
c=22
print(id(c))
'''
#---------------------------------
# x, y, z = 1, 2, 76
# print(x)
# print(y)
# print(z)
#_-------------------------------
# data = 1, 2, 76
# x, y, z = data
# print(x)
# print(y)
# print(z)
# ------------------------------
# data = 1, 2, 76 #זהו טאפל
# x, y, z = data
# print(x)
# print(y)
# print(z)
#------------------------------
# data_list = [1, 2, 76]
# x, y, z = data_list
# print(x)
# print(y)
# print(z)
#--------------------------------
# for index, name in enumerate(names):
# print(f"{index + 1}. {name}") # the tuples were unpacked
#--------------------------------
# for tutian in enumerate("abcdefgh"):
# print(tutian) # will show us tuples
#------------------------------------
# for t in enumerate("abcdefgh"):
# index, character = t # unpacking the tuple ...
# print(index, character)
#--------------------------------
# מבחן סלייסים
#letters = "abcdefghijklmnopqrstuvwxyz"
# print(letters[16:13:-1])
# print(letters[-22:-27:-1])
# print(letters[:-9:-1])
#---------------------------------------

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = 0
        self.perimeter = 0

    def area(self):
        self.area = self.width * self.height
        print("the area of the rectangle is %.2f" % self.area)

    def perimeter(self):
        self.perimeter = (self.width + self.height) * 2
        print("the area of rectangle is %.2f" % self.perimeter)

    def get_num():
        width = int(input("Enter the width of the rectangle: "))
        height = int(input("Enter the height of the rectangle: "))
        return width, height

updata = Rectangle.get_num()
Rectangle.area()
Rectangle.perimeter()









