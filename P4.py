# Project Euler Problem 5
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91x99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def pal(n):
	n = str(n)
	return n == n[::-1]

def paltest():
	from itertools import product
	print max(x * y for x, y in product(range(1000), repeat=2) if pal(x * y))
