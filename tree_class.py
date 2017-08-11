#tree class

class BTree(Tree):
	empty = tree(None)

	

class Tree:
	def __init__(self,root,branches=[]):
		self.root = root
		for branch in branches:
			assert isinstance(branch, Tree)
		self.branches = list(branches)

	def __repr__(self):
		if self.branches:
			branch_str = ', ' + repr(self.branches)
		else:
			branch_str = ''
		return 'Tree({0}{1})'.format(self.root,branch_str)

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
	if n == 0 or n == 1:
		return Tree(n)
	else:
		left = fib_tree(n-2)
		right = fib_tree(n-1)
		fib_n = left.root + right.root
		return Tree(fib_n, [left,right])

def leaves(t):
	if t.is_leaf():
		return [t.root]
	else:
		return sum([leaves(b) for b in t.branches], [])

def prune_repeats(t, seen):
	t.branches = [b for b in t.branches if b not in seen]
	seen.append(t)
	for b in t.branches:
		prune_repeats(b,seen)

def hailstone(n):
	print(n)
	if n == 1:
		return 1
	elif n % 2 == 0:
		return 1 + hailstone(n // 2)
	else:
		return 1 + hailstone(3 * n + 1)

def is_int(x):
	return int(x) == x

def is_odd(x):
	return x % 2 == 1

def hailstone_tree(k, n = 1):
	if k == 1:
		return Tree(n)
	else:
		greater, less = 2 * n, (n-1)/3
		branches = []
		branches.append(hailstone_tree(k-1, greater))
		if less > 1 and is_int(less) and is_odd(less): #BUG
			branches.append(hailstone_tree(k-1,int(less)))
		return Tree(n, branches)

def longest_path_below(k,t):
	if t.root > k:
		return []
	elif t.is_leaf():
		return [t.root]
	else:
		paths = [longest_path_below(k,b) for b in t.branches]
		return [t.root] + max(paths, key=len)