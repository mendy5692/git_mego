'''
from turtle import Turtle, Screen
import random

timmy = Turtle()
colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]
num_of_move = 3

for _ in range(10):
    timmy.color(random.choice(colors))
    for i in range(num_of_move):
        timmy.forward(50)
        timmy.right(360 / num_of_move)
    num_of_move += 1

screen = Screen()
screen.exitonclick()
'''
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.pensize(15)
timmy.hideturtle()
timmy.speed(15)


random_forward = [0,30]
random_right = [90 , 180, 270, 360]

for _ in range(120):
    timmy.color(random.choice(["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]))
    timmy.forward(random.choice(random_forward))
    timmy.right(random.choice(random_right))

screen = Screen()
screen.exitonclick()




