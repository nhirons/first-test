# float arithmetic

one = 0
for _ in range(10):
    one += 1/10

# Rational arithmetic

def add_rational(x, y):
    """Add rational numbers x and y."""
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rational(x, y):
    """Multiply rational numbers x and y."""
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def rationals_are_equal(x, y):
    """Return whether rational numbers x and y are equal."""
    return numer(x) * denom(y) == numer(y) * denom(x)

def print_rational(x):
    """Print rational x."""
    print(numer(x), "/", denom(x))


# Constructor and Selectors

def rational(n, d):
    """Construct a rational number x that represents n/d."""
    return [n, d]

def numer(x):
    """Return the numerator of rational number x."""
    return x[0]

def denom(x):
    """Return the denominator of rational number x."""
    return x[1]

r1 = rational(1, 2)
r2 = rational(1, 3)
r3 = mul_rational(r1, r2) # 1/2 * 1/3 = 1/6 
print_rational(r3)
r4 = add_rational(r2, r3) # 1/3 + 1/6 = 1/2
print_rational(r4) # what happened?

# Improved constructor

from fractions import gcd
def rational(n, d):
    """Construct a rational that represents n/d in lowest terms."""
    g = gcd(n, d)
    return [n//g, d//g]

# Functional Representation

def rational(n, d):
    """Consturct a functional representation of n/d."""
    g = gcd(n, d)
    n, d = n//g, d//g
    def select(name):
        if name == 'n':
            return n
        elif name == 'd':
            return d
    return select

def numer(x):
    """Return the numerator of functional rational number x."""
    return x('n')

def denom(x):
    """Return the denominator of functional rational number x."""
    return x('d')