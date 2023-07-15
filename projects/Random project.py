import math
def add(x, y):
    return x+y
def subtract(x, y):
    return x-y
def multiply(x, y):
    return x*y
def divide(x, y):
    return x/y
x = float(input("Enter your first number"))
y = float(input("Enter your second number"))
function = input("""Enter the function that you would like to use. Here are the options:
1. add
2. subtract
3. multiply
4. divide
Write the function that you would like to use.
eg. \"add\"""")
result = match function:
    case "add":
        return add(x, y)
    case "subtract":
        return subtract(x, y)
    case "multiply":
        return multiply(x, y)
    case "divide":
        return divide(x, y)
    case _:
        return "Error"

