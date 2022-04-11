'''
Citation of source code:
Title: Colorful Spiral
Author: Estefania Cassingena Navone
Date: Unknown
Code Version: Python 3.6
Availability: Udemy
'''

import turtle
import tkinter
from random import randint

turtle.title('See the spiral!')
turtle.bgcolor("black")

turtle.speed(0)
turtle.pensize(2)

def spiral_shape():
    side1 = 5
    for i in range(180):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)

        turtle.colormode(255)
        turtle.color(r, g, b)

        turtle.forward(side1)
        turtle.left(47)

        side1 += 4
    return side1

spiral_shape()