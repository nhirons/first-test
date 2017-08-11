# Abstraction

from math import sqrt
def hypotenuse(a, b):
    """
    >>> hypotenuse(3, 4)
    5.0
    >>> hypotenuse(5, 12)
    13.0
    """
    return sqrt(square(a) + square(b))

# Lambda Expressions

x = 10
x
square = x * x
square
square = lambda x: x * x
square
square(4)

def square(x):
    return x*x

# Environment Diagrams

def add_one(x):
    y = x + 1
    return y

def f(x, y):
    return g(x)

def g(z):
    return z + x
