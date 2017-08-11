def countdown(n):
	if n > 0:
		print(n)
		countdown(n-1)

def countup(n):
	if n > 0:
		countup(n-1)
		print(n)

def expt_iter(base, power):
	total = 1
	while power > 0:
		total = total * base
		power -= 1
	return total

def expt_rec(base, power):
	if power == 0:
		return 1
	else:
		return base * expt_rec(base, power - 1)

def count_stair_ways(n):
	if n == 0 or n == 1:
		return 1
	else:
		return count_stair_ways(n-1) + count_stair_ways(n-2)

def paths(m,n):
	if n==1 or m==1:
		return 1
	else:
		return paths(m-1,n) + paths(m,n-1)

def has_sum(total,n1,n2):
	if total % n1 == 0 or total % n2 == 0:
		return True
	elif total < min(n1, n2):
		return False
	else:
		return has_sum(total - n1,n1,n2) or has_sum(total -n2,n1,n2)

def has_sum_help(total,n1,n2):
	def helper(i):
		if i % n1 == 0 or i % n2 == 0:
			return True
		elif i < min(n1,n2):
			return False
		else:
			return helper(i - n1) or helper(i - n2)
	return helper(total)

def sum_range(lower,upper):
	def sum_range_heper(print_min, print_max):
		if lower <= print_min and print_max <= upper:
			return True
		if upper < print_min:
			return False
			return sum_range(print_min + 50, print_max + 60) or
				sum_range(print_min + 130, print_max + 140)
	return sum_range(0,0)
