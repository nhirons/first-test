from lab03 import *

def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: y * 10 + x % 10
    while x > 0:
        x, y = x // 10, f()
    return y == n

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return n * skip_mul(n - 2)

def count_up(n):
    """Print out all numbers up to and including n in ascending order.

    >>> count_up(5)
    1
    2
    3
    4
    5
    """
    def counter(i):
        if i <= n:
            print(i)
            return counter(i+1)
    counter(1)

def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    "*** YOUR CODE HERE ***"
    if b == 0:
        return c
    return a + ab_plus_c(a,b-1,c)


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def isnt_factor(i):
        if i > (n ** 0.5):
            return True
        elif n % i ==0:
            return False
        return isnt_factor(i+1)
    return isnt_factor(2)

def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 0
    if n == 1:
        return odd_term(1)

    def even_helper(i):
        if i == n:
            return even_term(i)
        return even_term(i) + odd_helper(i+1)

    def odd_helper(i):
        if i == n:
            return odd_term(i)
        return odd_term(i) + even_helper(i+1)

    return odd_term(1) + even_helper(2)


def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """

    if n == 0:
        return 0
    else:
        return ten_pairs(n//10) + count_digits(10 - n % 10, n//10)

def count_digits(i, n):
    if n == 0:
        return 0
    elif n % 10 == i:
        return 1 + count_digits(i, n // 10)
    else:
        return count_digits(i, n // 10)

def ten_pairs_nick(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    def digit_counter(i, n):
        if n == 0:
            return 0
        elif (n % 10) == i:
            return 1 + digit_counter(i, n // 10)
        return digit_counter(i, n // 10)

    def pair_counter(i, n):
        if n == 0:
            return 0
        elif (n % 10) == 10 - i:
            return 1 + pair_counter(i, n // 10)
        return pair_counter(i, n // 10)

    def n_choose_k(n,k):
        if n < k:
            return 0
        elif (k == 0) or (n == k):
            return 1
        else:
            return n_choose_k(n-1,k-1) + n_choose_k(n-1,k)

    def total_pair_helper(i):
        if i == 5:
            fives = digit_counter(5,n)
            return n_choose_k(fives, 2)
        else:
            digit_count = digit_counter(i,n)
            pair_count = pair_counter(i,n)
            pairs = digit_count * pair_count
            return pairs + total_pair_helper(i+1)

    return total_pair_helper(1)


def n_choose_k(n,k):
    if n < k:
        return 0
    elif (k == 0) or (n == k):
        return 1
    else:
        return n_choose_k(n-1,k-1) + n_choose_k(n-1,k)


def sum_to_n(n):
    total = 0
    while i <= n:
        total = total + i
        i += 1
    return total

def sum_to_n_recursive(n):
    if n == 0:
        return 0
    return n + sum_to_n_recursive(n-1)