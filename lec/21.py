# Trees

class Tree:
    """A tree with root as its root value."""
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

def leaves(tree):
    """Return the leaf values of a tree.

    >>> leaves(fib_tree(4))
    [0, 1, 1, 0, 1]
    """
    if tree.is_leaf():
        return [tree.root]
    else:
        return sum([leaves(b) for b in tree.branches], [])

# Binary trees

class BTree(Tree):
    """A tree with exactly two branches, which may be empty."""
    empty = Tree(None)

    def __init__(self, root, left=empty, right=empty):
        for b in (left, right):
            assert isinstance(b, BTree) or b is BTree.empty
        Tree.__init__(self, root, (left, right))

    @property
    def left(self):
        return self.branches[0]

    @property
    def right(self):
        return self.branches[1]

    def is_leaf(self):
        return [self.left, self.right] == [BTree.empty] * 2

    def __repr__(self):
        if self.is_leaf():
            return 'BTree({0})'.format(self.root)
        elif self.right is BTree.empty:
            left = repr(self.left)
            return 'BTree({0}, {1})'.format(self.root, left)
        else:
            left, right = repr(self.left), repr(self.right)
            if self.left is BTree.empty:
                left = 'BTree.empty' 
            template = 'BTree({0}, {1}, {2})'
            return template.format(self.root, left, right)

def fib_tree(n):
    """Fibonacci binary tree.

    >>> fib_tree(3)
    BTree(2, BTree(1), BTree(1, BTree(0), BTree(1)))
    """
    if n == 0 or n == 1:
        return BTree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        fib_n = left.root + right.root
        return BTree(fib_n, left, right)

def contents(t):
    """The values in a binary tree.

    >>> contents(fib_tree(5))
    [1, 2, 0, 1, 1, 5, 0, 1, 1, 3, 1, 2, 0, 1, 1]
    """
    if t is BTree.empty:
        return []
    else:
        return contents(t.left) + [t.root] + contents(t.right)

# Binary search trees

def bst(values):
    """Create a balanced binary search tree from a sorted list.

    >>> bst([1, 3, 5, 7, 9, 11, 13])
    BTree(7, BTree(3, BTree(1), BTree(5)), BTree(11, BTree(9), BTree(13)))
    """
    if not values:
        return BTree.empty
    mid = len(values) // 2
    left, right = bst(values[:mid]), bst(values[mid+1:])
    return BTree(values[mid], left, right)

def largest(t):
    """Return the largest element in a binary search tree.

    >>> largest(bst([1, 3, 5, 7, 9]))
    9
    """
    if t.right is BTree.empty:
        return t.root
    else:
        return largest(t.right)

def second(t):
    """Return the second largest element in a binary search tree.

    >>> second(bst([1, 3, 5]))
    3
    >>> second(bst([1, 3, 5, 7, 9]))
    7
    >>> second(Tree(1))
    """
    if t.is_leaf():
        return None
    elif t.right is BTree.empty:
        return largest(t.left)
    elif t.right.is_leaf():
        return t.root
    else:
        return second(t.right)

# Sets as binary search trees

def contains(s, v):
    """Return true if set s contains value v as an element.

    >>> t = BTree(2, BTree(1), BTree(3))
    >>> contains(t, 3)
    True
    >>> contains(t, 0)
    False
    >>> contains(bst(range(20, 60, 2)), 34)
    True
    """
    if s is BTree.empty:
        return False
    elif s.root == v:
        return True
    elif s.root < v:
        return contains(s.right, v)
    elif s.root > v:
        return contains(s.left, v)

def adjoin(s, v):
    """Return a set containing all elements of s and element v.

    >>> b = bst(range(1, 10, 2))
    >>> adjoin(b, 5) # already contains 5
    BTree(5, BTree(3, BTree(1)), BTree(9, BTree(7)))
    >>> adjoin(b, 6)
    BTree(5, BTree(3, BTree(1)), BTree(9, BTree(7, BTree(6))))
    >>> contents(adjoin(adjoin(b, 6), 2))
    [1, 2, 3, 5, 6, 7, 9]
    """
    if s is BTree.empty:
        return BTree(v)
    elif s.root == v:
        return s
    elif s.root < v:
        return BTree(s.root, s.left, adjoin(s.right, v))
    elif s.root > v:
        return BTree(s.root, adjoin(s.left, v), s.right)

