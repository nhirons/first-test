from math import sqrt

def is_prime(n):
	if n == 1:
		return False
	k = 2
	while k < (n**0.5):
		if not (n % k):
			k += 1
		else:
			return True
	return False
