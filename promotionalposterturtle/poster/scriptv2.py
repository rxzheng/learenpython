import turtle
import _tkinter as tk
import sys
sys.stdin = open("hexifier.txt", "r")
hexl = []
hexl = list(input().split())
# Set up the Turtle screen
screen = turtle.Screen()
screen.setup(900, 1200)

# Create a Turtle object
t = turtle.Turtle()
t.speed(0)  # Set the drawing speed (0 is the fastest)
turtle.tracer(0, 0)

# Set the initial position for drawing
x, y = -800, 500

# Set the size of each square
square_size = 5

# Loop through the list of hex color codes and draw squares
for hex_code in hexl:
    t.penup()
    t.goto(x, y)
    t.fillcolor(hex_code)  # Set the fill color to the hex code
    t.begin_fill()  # Start filling
    for _ in range(4):  # Draw a square
        t.forward(square_size)
        t.right(90)
    t.end_fill()  # End filling

    # Move to the next position
    if x < 100:
        x += square_size
    else:
        x = -800
        y = y + 5
turtle.update


# Close the Turtle window on click
screen.exitonclick()
