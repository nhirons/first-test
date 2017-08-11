def tree(root, branches=[]):
	for branch in branches:
		assert is_tree(branch)
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

def fib_tree(n):
	if n <= 1:
		return tree(n)
	else:
		left,right = fib_tree(n-2), fib_tree(n-1)
		return tree(root(left) + root(right), [left, right])

def count_leaves(t):
	if is_leaf(t):
		return 1
	else:
		branch_counts = [count_leaves(b) for b in branches(t)]
	return sum(branch_counts)

def leaves(tree):
	if is_leaf(tree):
		return [root(tree)]
	else:
		return sum([leaves(b) for b in branches(tree)], [])

def increment_leaves(t):
	if is_leaf(t):
		return tree(root(t) + 1)
	else:
		bs = [increment_leaves(b) for b in branches(t)]
		return tree(root(t), bs)

def increment(t):
	return tree(root(t) + 1, [increment(b) for b in branches(t)])

def print_tree(t, indent = 0):
	print('  ' * indent + str(root(t)))
	for b in branches(t):
		print_tree(b, indent + 1)