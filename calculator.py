"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math
def add(a, b):
    return a + b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    try:
        return b/a
    except ZeroDivisionError as error:
        print(error)
def logarithm(a, b):
    try:
        math.log(a, b)
    except ValueError as error:
        print(error)
def exponent(a, b):
    return a**b

