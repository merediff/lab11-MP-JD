
import math
def square_root(a):
    try:
        math.sqrt(a)
        if a < 0:
            raise ValueError("a cannot be negative")
    except ValueError as error:
        print(error)
def hypotenuse(a, b):
    return math.hypot(a, b)
def add(a, b):
    return a + b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    if a == 0:
        return ZeroDivisionError
    return b/a
def logarithm(a, b):
    try:
        math.log(a, b)
    except ValueError as error:
        print(error)
def exponent(a, b):
    return a**b

