# Print and None

-2
print(-2)
'Go Bears'
print('Go Bears')
print(1, 2, 3)
None
print(None)
x = -2
x
x = print(-2)
x


# Print and Return

def favorite():
    return 'Stanfield Chu'

my_love = favorite()
my_love
'I love ' + my_love

def favorite():
    print('Stanfield Chu')

my_love = favorite()
my_love  # None not displayed
# 'I love ' + my_love  # gives an error


# Nested expressions

print(print(1), print(2))


# Conditional expressions

def absolute_value(x):
    """Return the absolute value of x.

    >>> absolute_value(-3)
    3
    >>> absolute_value(3)
    3
    """
    if x < 0:
        return -x
    else:
        return x


# Boolean expressions

not 1
not 0
False and True
True or False
# 1/0  # gives an error
0 and 1/0
# 0 or 1/0  # gives an error
1 and 2 and 3 and 'Hi!'


# Iteration

def factorial(n):
    """Return the factorial of n.

    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    """
    i, total = 1, 1
    while i < n:
        i += 1
        total *= i
    return total


# Sequences

def factorial(n):
    """Return the factorial of n.

    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    """
    total = 1
    for i in range(1, n+1):
        total *= i
    return total
