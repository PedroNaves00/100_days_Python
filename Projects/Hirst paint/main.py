"""import colorgram

colors = colorgram.extract("image.jpg", 30)
colors_rgb = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    colors_rgb.append(new_color)

print(colors_rgb)"""
import turtle as turtle_module
import random

turtle_module.colormode(255)
bob = turtle_module.Turtle()
bob.speed("fastest")
bob.penup()
bob.hideturtle()
color_list = [(202, 164, 110),  (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

bob.setheading(225)
bob.forward(300)
bob.setheading(0)
numbers_of_dots = 100

for dot_count in range(1, numbers_of_dots + 1):
    bob.dot(20, random.choice(color_list))
    bob.forward(50)

    if dot_count % 10 == 0:
        bob.setheading(90)
        bob.forward(50)
        bob.setheading(180)
        bob.forward(500)
        bob.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()

