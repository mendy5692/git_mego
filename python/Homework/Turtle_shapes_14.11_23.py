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