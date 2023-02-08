import turtle
from turtle import Turtle, Screen
import random

pedro = Turtle()
pedro.shape("turtle")
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


pedro.speed("fastest")


def draw(size_of_gap):
    for x in range(int(360 / size_of_gap)):
        pedro.color(random_color())
        pedro.circle(100)
        pedro.setheading(pedro.heading() + size_of_gap)


draw(2)

screen = Screen()
screen.exitonclick()
