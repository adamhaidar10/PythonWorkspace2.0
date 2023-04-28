from turtle import pencolor, left, right, forward, fillcolor, reset, speed
from turtle import begin_fill, penup, pendown, end_fill, colormode, exitonclick

import random


def square():
    speed(15)
    r, g, b = (
        random.randint(0, 255),
        random.randint(0, 255),
    )
    random.randint(0, 255)
    fill = (r, g, b)
    fillcolor(fill)

    pen = (r, g, b)
    pencolor(pen)

    pendown()
    begin_fill()
    for i in range(1, 5):
        forward(200)
        right(90)
    end_fill()
    penup()


reset()
colormode(255)

for i in range(1, 17):
    square()
    right(45)
    forward(50)
    left(20)

exitonclick()

""" for i in range(1, 5):
    pendown()
    circle(radius = 150, steps = 6)
    penup()
    right(45)
    forward(50)
    left(45) """
exitonclick()
