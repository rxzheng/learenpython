from turtle import *

pensize(10)
count = 30

setheading(180)
def move():
    global count
    forward(count)
    left(90)
    count += 30

while True:
    color("red")
    move()
    move()
    color("blue")
    move()
    move()
