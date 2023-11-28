from turtle import Turtle, Screen
from random import randint

Screen().colormode(255)

timmy = Turtle()
timmy.speed(12)
timmy.hideturtle()

while True:
    timmy.color(randint(1, 255), randint(1, 255), randint(1, 255))
    timmy.circle(100)
    timmy.left(10)

screen = Screen()
screen.exitonclick()