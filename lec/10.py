# Trees

def tree(root, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root] + list(branches)

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

### +++ === ABSTRACTION BARRIER === +++ ###

# Processing Trees

def count_nodes(t):
    """The number of nodes in tree.

    >>> count_nodes(tree(8, [tree(4, [tree(2), tree(3)]), tree(3, [tree(1), tree(1, [tree(1), tree(1)])])]))
    9
    """
    if is_leaf(t):
        return 1
    else:
        return 1 + sum([count_nodes(b) for b in branches(t)])

def leaves(t):
    """
    >>> leaves(tree('D', [tree('B', [tree('A'), tree('C')]), tree('F', [tree('E'), tree('H', [tree('G'), tree('I')])])]))
    ['A', 'C', 'E', 'G', 'I']
    """
    if is_leaf(t):
        return [root(t)]
    _leaves = []
    for b in branches(t):
        _leaves += leaves(b)
    return _leaves

# Printing Trees

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the entry.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> print_tree(fib_tree(4))
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
    print('  ' * indent + str(root(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

# Creating Trees

def square_tree(t):
    """
    >>> t = square_tree(tree(8, [tree(4, [tree(2), tree(3)]), tree(3, [tree(9), tree(6)])]))
    >>> print_tree(t)
    64
      16
        4
        9
      9
        81
        36
    """
    new_root = root(t) * root(t)
    new_branches = [square_tree(b) for b in branches(t)] 
    return tree(new_root, new_branches)

def fib_tree(n):
    """Construct a Fibonacci tree.

    >>> print_tree(fib_tree(1))
    1
    >>> print_tree(fib_tree(2))
    1
      0
      1
    >>> print_tree(fib_tree(3))
    2
      1
      1
        0
        1
    >>> print_tree(fib_tree(5))
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
    """
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        fib_n = root(left) + root(right)
        return tree(fib_n, [left, right])
