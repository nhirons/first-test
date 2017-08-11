def square(x):
    return x * x

# Evaluation Review
def a_plus_bc(a, b, c):
    """
    >>> a_plus_bc(2, 3, 4) # 2 + 3 * 4
    14
    """
    bc = b * c
    return a + bc

# Printing Review

print(5)
square(5)
print(square(5))
print(1, 2)
print(print(1), square(2), print(square(3)))

def square_and_print(x):
    squared = square(x)
    print(squared)
    return squared

square_and_print(5)
print(square_and_print(5))
print(print(1), square_and_print(2), print(square_and_print(3)))

# Designing Functions

def square(x):
    return x * x

# Generalization

def sum_naturals(n):
    """
    >>> sum_naturals(5)
    15
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total

def sum_cubes(n):
    """
    >>> sum_cubes(5)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + pow(k, 3), k + 1
    return total

def summation(n, term):
    """
    >>> summation(5, lambda x: x) # identity
    15
    >>> summation(5, lambda x: pow(x, 3)) # cube
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

# Returning Functions

def make_adder(n):
    """
    Return a function that takes one argument k, and returns k + n.

    >>> add_ten = make_adder(10)
    >>> add_ten(15)
    25
    """
    def adder(k):
        return n + k
    return adder

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h
