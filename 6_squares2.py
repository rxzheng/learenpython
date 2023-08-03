from turtle import *

penup()
pensize(10)
color("green")
goto(-365, 300)
pendown()
setheading(180)

def square():
    for i in range(4):
        forward(100)
        right(90)

square()

penup()
color("red")
goto(265, 200)
square()
