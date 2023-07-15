from enum import Enum

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

#tuple

#sets
set1 = {"Roger", "Matt"}
set2 = {"Roger"}
print(set1 > set2)

#functsion
def hello(name):
    print ("Hello " + name)
hello("Richard")

def hi():
    count = 1
    def test():
        nonlocal count
        print(count)
    print(test())
hi()

#objects
age = 8
print(age.real)
print(age.imag)
items = [1, 2, 3, 4]
print(items)
#loops
while True:
    print("This conditions is true")
    break
for item in range(10):
    print(item)
for index, item in enumerate(items):
    print(index, item)
#class
class Animal:
    def walk(self):
        print("Walking")
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print ("woof")
roger = Dog("Roger", 9)
print(roger.name)
print(roger.age)
roger.bark()
#modules

from math import sqrt
print(sqrt(4))
 #lambda
multiply = lambda a, b: a * b
print(multiply(1, 2))
