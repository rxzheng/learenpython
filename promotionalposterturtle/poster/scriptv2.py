import turtle
import _tkinter as tk
import sys
sys.stdin = open("hexcodes.txt", "r")
hexl = []
hexl = list(input().split())
# Set up the Turtle screen
screen = turtle.Screen()
screen.setup(400, 400)

# Create a Turtle object
t = turtle.Turtle()
t.speed(0)  # Set the drawing speed (0 is the fastest)

# Set the initial position for drawing
x, y = -100, 100

# Set the size of each square
square_size = 20

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
    x += square_size

# Close the Turtle window on click
screen.exitonclick()