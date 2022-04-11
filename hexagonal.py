import turtle
import tkinter
from random import randint

turtle.title("Hexagonal!")
turtle.bgcolor("black")
turtle.speed(0)
turtle.pensize(2)


def point_spiral():
    side_1 = 5
    side_2 = 2

    for i in range(180):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)

        turtle.colormode(255)
        turtle.color(r, g, b)

        turtle.forward(side_1)
        turtle.backward(side_2)
        turtle.left(47)
        turtle.right(120)

        side_1 += 4
        side_2 += 3
    return side_1, side_2

point_spiral()