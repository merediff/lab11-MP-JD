import math

def add(a, b):
    return a + b
def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

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
def logarithm(a, b):
    try:
        math.log(a, b)
    except ValueError as error:
        print(error)
def exponent(a, b):
    return a**b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def log(a, b):
    if a <= 0:
        raise ValueError
    if b <= 0 or b == 1:
        raise ValueError
    return math.log(a,b)

def exp(a, b):
    return a**b