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