import math

def add(a, b):
    return a + b

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

def subtract(a, b):
    return a-b

def logarithm(a, b):
    try:
        math.log(a, b)
    except ValueError as error:
        print(error)


def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a


def exp(a, b):
    return a**b