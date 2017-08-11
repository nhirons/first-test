# Recursive factorial

def factorial(n):
    """Return the factorial of n.

    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# Sum digits

def sum_digits(n):
    """Return the sum of the digits of positive integer n.

    >>> sum_digits(9)
    9
    >>> sum_digits(18117)
    18
    >>> sum_digits(9437184)
    36
    >>> sum_digits(11408855402054064613470328848384)
    126
    """
    if n < 10:
        return n
    else:
        return sum_digits(n//10) + n%10


# Count up to a number with print expressions
# With recursion by enumeration first since it's a bit easier to demonstrate

def count_up(n):
    """Recursively print up to n.

    >>> count_up(5)
    1
    2
    3
    4
    5
    """
    if n == 1:
        print(1)
    elif n == 2:
        print(1)
        print(2)
    elif n == 3:
        print(1)
        print(2)
        print(3)
    elif n == 4:
        count_up(3)
        print(4)
    else:
        count_up(n - 1)
        print(n)


# Now, a cleaned-up version

def count_up(n):
    """Recursively print up to n.

    >>> count_up(5)
    1
    2
    3
    4
    5
    """
    if n >= 1:
        count_up(n - 1)
        print(n)


# Iterative factorial
# Key idea in converting recursion to iteration: try to make the state
# maintained in each iteration the same as the state maintained by each
# recursive call

def fact_iter(n):
    total, k = 1, 1
    while k <= n:
        total, k = total * k, k + 1
    return total


# Converting back to recursion
# More formulaic: whatever state is maintained in each iteration, pass
# that in as arguments to the recursive function

def fact2(n, total):
    if n == 0:
        return total
    else:
        return fact2(n-1, total*n)

# Can be ugly or complicated, but often not too hard to clean up

fact = lambda n: fact2(n, 1)

