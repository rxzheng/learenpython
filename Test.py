import math
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y
def power(x, y):
    return x ** y
def divide (x, y):
    return x / y

def root (x, y):
    return (math.sqrt(x))
def sin (x, y):
    return (math.sin(math.radians(x)))
def cos (x, y):
    return (math.cos(math.radians(x)))
def tan (x, y):
    return (math.cos(math.degrees(x)))

print (""" Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Root (first number)
6. Sine (first number)
7. Cosine (first number)
8. Tangent (first number)""")
       
while True:
    choice = input("Enter choice(1/2/3/4/5/6): ")

    if choice in ('1', '2', '3', '4', '5', '6', '7', '8'):
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))

        if choice == '1':
            print (add(num1, num2))
                     
        elif choice == '2':
            print (subtract(num1, num2))
            
        elif choice == '3':
            print (multiply(num1, num2))
        
        elif choice == '4':
            print (divide(num1, num2))
        elif choice == '5':
            print (root(num1, num2))
        elif choice == '6':
            print (sin(num1, num2)) 
        elif choice == '7':
            print (cos(num1 , num2))
        elif choice == '8':
            print (tan(num1, num2))

    else:
        print ("Invalid")
    
