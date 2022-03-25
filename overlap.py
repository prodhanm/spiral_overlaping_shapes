import turtle
import tkinter
from random import randint

turtle.bgcolor("black")

turtle.speed(0)
turtle.pensize(2)

def spiral_shape():
    side = 5
    for i in range(180):
        for j in range(180):
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)

            turtle.colormode(255)
            turtle.color(r, g, b)

            turtle.forward(side)
            turtle.left(45)

            side += 2
    return side

spiral_shape()