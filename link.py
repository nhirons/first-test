from math import sqrt

def empty(s):
	return s is Link.empty

def contains(s, v):
	"""Return true if sets s contains value x as an element.
	>>> s = Link(1, Link(3, Link(2)))
	>>> contains(s, 2)
	True
	>>> contains(s, 5)
	False
	"""
	if empty(s) or s.first > v:
		return False
	elif s.first == v:
		return True
	else:
		return contains(s.rest,v)

def adjoin(s, v):
	if empty(s) or v < s.first:
		return Link(v, s)
	elif v == s.first:
		return s
	else:
		return Link(s.first, adjoin(s.rest,v))

def intersect(set1, set2):
	if empty(set1) or empty(set2):
		return Link.empty
	else:
		e1, e2 = set1.first, set2.first
		if e1 == e2:
			return Link(e1, intersect(set1.rest, set2.rest))
		elif e1 < e2:
			return intersect(set1.rest, set2)
		elif e2 < e1:
			return intersect(set, set2.rest)

def union(set1, set2):
	if empty(set1):
		return set2
	elif empty(set2):
		return set1
	else:
		e1, e2 = set1.first. set2.rest_str
		if e1 == e2:
			return Link(e1, union(set1.rest, set2.rest))
		elif e1 < e2:
			return Link(e1, union(set1.rest, set2))
		elif e2 < e1:
			return Link(e2, union(set1, set2.rest))
	not_in_set2 = lambda v: not contains(set2, v)
	set1_not_set2 = filter_link(not_on_set2, set1)
	return extend_link(set1_not_set2, set2)

def add(s, v):
	assert not empty(s)
	if s.first > v:
		s.first, s.rest = v, Link(s.first, s.rest)
	elif s.first < v and empty(s.rest):
		s.rest = Link(v, s.rest)
	elif s.first < v:
		add(s.rest, v)
	return s

class Link:

	empty = ()

	def __init__(self, first, rest = empty):
		assert rest is Link.empty or isinstance(rest, Link)
		self.first = first
		self.rest = rest

	def __repr__(self):
		if self.rest:
			rest_str = ', ' + repr(self.rest)
		else:
			rest_str = ''
		return 'Link({0}{1})'.format(self.first, rest_str)

	def __getitem__(self, i):
		if i == 0:
			return self.first
		else:
			return self.rest[i-1] #element selection syntax

	def __len__(self):
		return 1 + len(self.rest)

	@property #don't need to write s.second(), only s.second
	def second(self):
		return self.rest.first

	@second.setter #supports assignment s.second = 6 etc.
	def second(self, value):
		self.rest.first = value

# s = Link(3, Link(4, Link(5)))
# square = lambda x: x * x
# odd = lambda x: x % 2 == 1

def extend_link(s, t):

	if s is Link.empty:
		return t
	else:
		return Link(s.first, extend_link(s.rest,t))

def map_link(f, s):
	if s is Link.empty:
		return s
	else:
		return Link(f(s.first), map_link(f, s.rest))

def filter_link(f, s):
	if s is Link.empty:
		return s
	else:
		filtered = filter_link(f, s.rest)
		if f(s.first):
			return Link(s.first, filtered)
		else:
			return filtered

def join_link(s,separator):
	if s is Link.empty:
		return ""
	elif s.rest is Link.empty:
		return str(s.first)
	else:
		return str(s.first)+separator+join_link(s.rest,separator)

def partitions(n, m):
	if n == 0:
		return Link(Link.empty)
	if n < 0 or m == 0:
		return Link.empty
	else:
		using_m = partitions(n-m,m)
		with_m = map_link(lambda p: Link(m,p), using_m)
		without_m = partitions(n,m-1)
		return extend_link(with_m, without_m)

def print_partitions(n, m):
	links = partitions(n, m)
	lines = map_link(lambda s: join_link(s, " + "), links)
	map_link(print, lines)