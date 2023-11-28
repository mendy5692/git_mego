from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.pensize(5)
tim.pencolor("blue")

screen = Screen()
screen.listen()
screen.bgcolor("yellow")

def mov_forwards():
    tim.forward(10)

def mov_back():
    tim.backward(10)

def mov_right():
    tim.right(20)

def mov_left():
    tim.left(20)

def new_painting():
    tim.home()
    tim.clear()

screen.onkey(key="w", fun=mov_forwards)
screen.onkey(key="s", fun=mov_back)
screen.onkey(key="d", fun=mov_right)
screen.onkey(key="a", fun=mov_left)
screen.onkey(key="c", fun=new_painting)

screen.exitonclick()