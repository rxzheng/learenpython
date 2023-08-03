from turtle import *

penup()
pensize(10)
color("green")
goto(-300, 260)
pendown()
setheading(180)

def square():
    for i in range(4):
        forward(100)
        right(90)

square()

penup()
color("red")
goto(260, -300)
pendown()
square()
