# Cycles

def cycle_demo():
    """A linked list can contain cycles.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.first = 5
    >>> t = s.rest
    >>> t.rest = s
    >>> s.first
    5
    >>> s.rest.rest.rest.rest.rest.first
    2
    """

# Bear Environment

def oski(bear):
    """Oski the bear.

    >>> oski(abs)
    [2, [3, 1]]
    """
    def cal(berk):
        nonlocal bear
        if bear(berk) == 0:
            return [berk+1, berk-1]
        bear = lambda ley: berk-ley
        return [berk, cal(berk)]
    return cal(2)

# Work

class Worker:
    greeting = 'Sir'
    def __init__(self):
        self.elf = Worker
    def work(self):
        return self.greeting + ', I work'
    def __repr__(self):
        return Bourgeoisie.greeting

class Bourgeoisie(Worker):
    greeting = 'Peon'
    def work(self):
        print(Worker.work(self))
        return 'My job is to gather wealth'

jack = Worker()
john = Bourgeoisie()
jack.greeting = 'Maam'

def work():
    """Working.

    >>> Worker().work()
    'Sir, I work'
    >>> jack
    Peon
    >>> jack.work()
    'Maam, I work'
    >>> john.work()
    Peon, I work
    'My job is to gather wealth'
    >>> john.elf.work(john)
    'Peon, I work'
    """

# Morse tree

abcde = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.'}

def morse(code):
    """Return a tree representing the code. Each non-root, non-leaf node is a
    signal. Each leaf node is a letter encoded by the path from the root.

    >>> print(morse(abcde))
    None
      .
        -
          a
        e
      -
        .
          .
            .
              b
            d
          -
            .
              c
    """
    root = Tree(None)
    for letter, signals in sorted(code.items()):
        tree = root
        for signal in signals:
            matches = [b for b in tree.branches if b.root == signal]
            if matches:
                assert len(matches) == 1
                tree = matches[0]
            else:
                branch = Tree(signal)
                tree.branches.append(branch)
                tree = branch
        tree.branches.append(Tree(letter))
    return root

def decode(signals, tree):
    """Decode signals into a letter.

    >>> t = morse(abcde)
    >>> [decode(s, t) for s in ['-..', '.', '-.-.', '.-', '-..', '.']]
    ['d', 'e', 'c', 'a', 'd', 'e']
    """
    for signal in signals:
        tree = [b for b in tree.branches if b.root == signal][0]
    leaves = [b for b in tree.branches if not b.branches]
    assert len(leaves) == 1
    return leaves[0].root

# Link & Tree

class Link:
    """A linked list."""
    empty=()
    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

class Tree:
    """A tree with root as its root value."""
    def __init__(self, root, branches=()):
        self.root = root
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)
    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(repr(self.root), branch_str)
    def __str__(self):
        return '\n'.join(self.indented())
    def indented(self, k=0):
        indented = []
        for b in self.branches:
            for line in b.indented(k + 1):
                indented.append('  ' + line)
        return [str(self.root)] + indented


