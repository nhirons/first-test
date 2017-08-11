from math import sqrt

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


class Ratio:

	def __init__(self, n, d):
		self.numer = n
		self.denom = d

	def __repr__(self):
		return 'Ratio({0},{1})'.format(self.numer,self.denom)

	def __str__(self):
		return '{0}/{1}'.format(self.numer,self.denom)

	def __add__(self,other):
		if isinstance(other,int):
			n = self.numer + self.denom * other
			d = self.denom
		elif isinstance(other, Ratio):
			n = self.numer * other.denom + self.denom * other.numer
			d = self.denom * other.denom
		elif isinstance(other,float):
			return float(self) + other
		g = gcd(n,d)
		return Ratio(n//g,d//g)

	__radd__ = __add__

	def __float__(self):
		return self.numer/self.denom


class Bear:

	def __init__(self):
		self.__repr__ = lambda: 'oski'
		self.__str__ = lambda: 'this bear'

	def __repr__(self):
		return 'Bear()'

	def __str__(self):
		return 'a bear'

# oski = Bear()
# print(oski)
# print(str(oski))
# print(repr(oski))
# print(oski.__str__())
# print(oski.__repr__())

def repr(x):
	return type(x).__repr__(x)

def str(x):
	t = type(x)
	if hasattr(t, '__str__'):
		return t.__str__(X)
	else:
		return repr(x)

class Account:
	interest = 0.02
	def __init__(self, account_holder):
		self.balance = 0
		self.holder = account_holder

	def deposit(self,amount):
		self.balance = self.balance + amount
		return self.balance

	def withdraw(self, amount):
		if amount > self.balance:
			return 'Insufficient funds'
		self.balance = self.balance - amount
		return self.balance

class CheckingAccount(Account):
	withdraw_fee = 1
	interest = 0.01
	def withdraw(self,amount):
		return Account.withdraw(self, amount + self.withdraw_fee)

class Bank:
	"""A bank *has* accounts.

	>>> bank = Bank()
	>>> john = bank.open_account('John', 10)
	>>> jack = bank.open_account('Jack', 5, CheckingAccount)
	>>> john.interest
	0.02
	>>> jack.interest
	0.01
	>>> bank.pay_interest()
	>>> john.balance
	10.2
	>>> bank.too_big_to_fail()
	True
	"""
	def __init__(self):
		self.accounts = []

	def open_account(self,holder,amount, kind = Account):
		account = kind(holder)
		account.deposit(amount)
		self.accounts.append(account)
		return account

	def pay_interest(self):
		for a in self.accounts:
			a.deposit(a.balance * a.interest)

	def too_big_to_fail(self):
		return len(self.accounts) > 1

class SavingsAccount(Account):
	deposit_fee = 2
	def deposit(self, amount):
		return Account.deposit(self, amount - self.deposit_fee)

class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
	def __init__(self,account_holder):
		self.holder = account_holder
		self.balance = 1			# A free dollar!


def make_withdraw(balance):
	def withdraw(amount):
		nonlocal balance
		if amount > balance:
			return 'Insufficient funds'
		balance = balance - amount
		return balance
	return withdraw

def exp(b,n):
	if n == 0:
		return 1
	return b * exp(b,n-1)

def fast_exp(b,n):
	if n == 1:
		return 1
	elif n % 2 == 0:
		return square(fast_exp(b,n//2))
	else:
		return b * fast_exp(b,n-1)


def divides(k,n):
	return n % k == 0

def factors(n):
	total = 0
	for k in range (1, n+1):
		if divides(k, n):
			total += 1
	return total

def factors_fast(n):
	total = 0
	sqrt_n = sqrt(n)
	k = 1
	while k < sqrt_n:
		if divides(k,n):
			total += 2
		k += 1
	if k*k == n:
		total += 1
	return total

def count_frames(f):
	def counted(n):
		counted.open_count += 1
		if counted.open_count > counted.max_count:
			counted.max_count = counted.open_count
		result = f(n)
		counted.open_count -= 1
		return result
	counted.open_count = 0
	counted.max_count = 0
	return counted

def fib(n):
	if n == 0 or n == 1:
		return n
	else:
		return fib(n-2) + fib(n-1)

def count(f):
	def counted(*args):
		counted.call_count += 1
		return f(*args)
	counted.call_count = 0
	return counted

def memo(f):
	cache = {}
	def memoized(n):
		if n not in cache:
			cache[n] = f(n)
		return cache[n]
	return memoized

def divisors(n):
	return [1] + [x for x in range(2,n) if n%x == 0]


def split(n):
	return n // 10, n % 10

def sum_digits(n):
	if n < 10:
		return n
	else:
		all_but_last, last = split(n)
		return sum_digits(all_but_last) + last

def sum_digits_iter(n):
	digit_sum = 0
	while n > 0:
		n, last = split(n)
		digit_sum = digit_sum + last
	return digit_sum

def sum_digits_rec(n, digit_sum):
	if n == 0:
		return digit_sum
	else:
		n, last = split(n)
		return sum_digits_rec(n, digit_sum + last)

def fact(n):
	if n == 0:
		return 1
	else:
		return n * fact(n-1)

def luhn_sum(n):
	if n < 10:
		return n
	else:
		all_but_last, last = split(n)
		return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
	all_but_last, last = split(n)
	luhn_digit = sum_digits(2 * last)
	if n < 10:
		return luhn_digit
	else:
		return luhn_sum(all_but_last) + luhn_digit

def cascade(n):
	if n < 10:
		print(n)
	else:
		print(n)
		cascade(n // 10)
		print(n)

def cascade_short(n):
	print(n)
	if n >= 10:
		cascade(n//10)
		print(n)

def inverse_cascade(n):
	grow(n)
	print(n)
	shrink(n)

def f_then_g(f, g, n):
	if n:
		f(n)
		g(n)

grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)

def grow_nick(n):
	if n//10:
		grow_nick(n//10)
		print(n//10)

def shrink_nick(n):
	if n//10:
		print(n//10)
		shrink(n//10)

def count_partitions(n, m):
	if n == 0:
		return 1
	elif n < 0:
		return 0
	elif m == 0:
		return 0
	else:
		with_m = count_partitions(n-m,m)
		without_m = count_partitions(n,m-1)
		return with_m + without_m

def gcd(m, n):
	""" Returns the largest k that divides both m and n

	k, m, n are all positive integers

	>>> gcd(12,8)
	4
	>>> gcd(16,12)
	4
	>>> gcd(16,8)
	8
	>>> gcd(2,16)
	2
	>>> gcd(5,5)
	5
	"""
	if n % m == 0:
		return m
	elif m < n:
		return gcd(n,m)
	else:
		return gcd(m-n, n)

def curry2(f):
	def g(x):
		def h(y):
			return f(x,y)
		return h
	return g


def trace1(fn):
	"""Returns a version of fn that first prints before it is called.

	fn - a function of 1 argument.
	"""
	def traced(x):
		print('Calling', fn, 'on argument', x)
		return fn(x)
	return traced

#@trace1 #this is a decorator, same as square = trace1(square) after
def square(x):
	return x*x

@trace1
def sum_squares(n):
	k = 1
	total = 0
	while k <= n:
		total, k = total + square(k), k+1
	return total
