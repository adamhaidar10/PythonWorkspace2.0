from turtle import pencolor, left, right, width, forward, back, fillcolor
from turtle import reset, speed, begin_fill, penup, goto, pendown
from turtle import circle, end_fill, setheading, exitonclick
import random


def f(n):
    if n > 0:
        print(f"The number is {n}")
        f(n - 1)


f(100)


def fact(n):
    if n > 1:
        return n * fact(n - 1)
    else:
        return n


print(fact(15))


"""def recursive_square(n):
    if n > 0:
        circle(n * 10)
        #for i in range(4):
       #     forward (100 + n * 10)
        #    right(90)

        penup()
        right(40)
        forward(20)
        left(20)
        pendown()

        recursive_square(n-1)
    reset()
    speed(0)
recursive_square(20) """

""" def tree(n):
    r, g, b = (83, 53, 10)
    pen = (r, g, b)
    pencolor(pen)
    if n > 4:
        width(n  / 20)
        forward(n)
        left(30)
        tree(n * 0.7)
        right(60)
        tree(n * 0.4)
        left(30)
        back(n)
    else:
        pencolor ("green")
        fillcolor("green")
        begin_fill()
        circle(random.randint(7, 15))
        end_fill()
reset()
penup()
goto(0, -350)
pendown()
left(90)
speed(0)
colormode(255)

tree(200)
exitonclick() """


def newtree(n):
    if n > 10:
        pencolor("brown")
        width(n * 0.1)
        forward(n)
        left(30)
        newtree(n * (random.randint(4, 8) / 10))
        right(60)
        newtree(n * (random.randint(4, 8) / 10))
        left(30)
        back(n)
    else:
        pencolor("black")
        fillcolor("pink")
        begin_fill()
        circle(random.randint(5, 15))
        end_fill()
        pencolor("brown")


reset()
speed(0)
penup()
goto(0, -300)
setheading(90)
pendown()

newtree(random.randint(150, 250))

exitonclick()
