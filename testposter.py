import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.title("Hanging Rock Poster")
screen.bgcolor("white")

# Create a turtle
poster_turtle = turtle.Turtle()
poster_turtle.speed(1)  # Set the drawing speed

# Draw the Hanging Rock outline
poster_turtle.penup()
poster_turtle.goto(0, -200)
poster_turtle.pendown()
poster_turtle.color("black")
poster_turtle.begin_fill()
poster_turtle.circle(200)
poster_turtle.end_fill()

# Add text to the poster
poster_turtle.penup()
poster_turtle.goto(0, 0)
poster_turtle.pendown()
poster_turtle.color("black")
poster_turtle.write("Hanging Rock", align="center", font=("Arial", 20, "bold"))

# Hide the turtle
poster_turtle.hideturtle()

# Display the poster
turtle.done()
