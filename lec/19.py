class Tree:
    """A tree is a root value and a list of branches."""
    def __init__(self, root, branches=[]):
        self.root = root
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.root, branch_str)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self, k=0):
        indented = []
        for b in self.branches:
            for line in b.indented(k + 1):
                indented.append('  ' + line)
        return [str(self.root)] + indented

    def is_leaf(self):
        return not self.branches

def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

@memo
def fib_tree(n):
    """A Fibonacci tree.

    >>> print(fib_tree(4))
    3
      1
        0
        1
      2
        1
        1
          0
          1
    """
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        fib_n = left.root + right.root
        return Tree(fib_n, [left, right])

def leaves(tree):
    """Return the leaf values of a tree.

    >>> leaves(fib_tree(4))
    [0, 1, 1, 0, 1]
    """
    if tree.is_leaf():
        return [tree.root]
    else:
        return sum([leaves(b) for b in tree.branches], [])

def prune(t, n):
    """Prune sub-trees whose root value is n.

    >>> t = fib_tree(5)
    >>> prune(t, 1)
    >>> print(t)
    5
      2
      3
        2
    """
    t.branches = [b for b in t.branches if b.root != n]
    for b in t.branches:
        prune(b, n)

def prune_repeats(t, seen):
    """Remove repeated sub-trees

    >>> def fib_tree(n):
    ...     if n == 0 or n == 1:
    ...         return Tree(n)
    ...     else:
    ...         left = fib_tree(n-2)
    ...         right = fib_tree(n-1)
    ...         return Tree(left.root + right.root, (left, right))
    >>> fib_tree = memo(fib_tree)
    >>> t = fib_tree(6)
    >>> print(t)
    8
      3
        1
          0
          1
        2
          1
          1
            0
            1
      5
        2
          1
          1
            0
            1
        3
          1
            0
            1
          2
            1
            1
              0
              1
    >>> prune_repeats(t, [])
    >>> print(t)
    8
      3
        1
          0
          1
        2
      5
    """
    t.branches = [b for b in t.branches if b not in seen]
    seen.append(t)
    for b in t.branches:
        prune_repeats(b, seen)

def hailstone(n):
    """Print a hailstone sequence and return its length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n//2)
    else:
        return 1 + hailstone(3*n+1)

def is_int(x):
    return int(x) == x

def is_odd(n):
    return n % 2 == 1

def hailstone_tree(k, n=1):
    """Build a tree in which paths are hailstone sequences.

    >>> hailstone_tree(6)
    Tree(1, [Tree(2, [Tree(4, [Tree(8, [Tree(16, [Tree(32), Tree(5)])])])])])
    >>> leaves(hailstone_tree(11))
    [1024, 170, 168, 160, 26, 24]
     """
    if k == 1:
        return Tree(n)
    else:
        greater, less = 2*n, (n-1)/3
        branches = [hailstone_tree(k-1, greater)]
        if less > 1 and is_int(less) and is_odd(less):
            branches.append(hailstone_tree(k-1, int(less)))
        return Tree(n, branches)

def longest_path_below(k, t):
    """Return the longest path through t of values all less than k.

    >>> longest_path_below(20, hailstone_tree(10))
    [1, 2, 4, 8, 16, 5, 10, 3, 6, 12]
    """
    if t.root >= k:
        return []
    elif t.is_leaf():
        return [t.root]
    else:
        paths = [longest_path_below(k, b) for b in t.branches]
        return [t.root] + max(paths, key=len)
