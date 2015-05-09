# Project Euler Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Personal Notes
# I learned about the "inclusion-exclusion principle" in completing this
# problem as I had to count all multiples of 3 & 5, but 
# exclude multiples of 15 as that is the intersection of 3 & 5  

# Code below

def p1(x):
	y = (x-1)/3
	z = (x-1)/5
	w = (x-1)/15
	total1 = 0
	total2 = 0
	total3 = 0
	while y >=0:
		total1 += 3 * y
		y-=1
	while z >=0:
		total2 += 5 * z
		z-=1
	while w >=0:
		total3 += 15 * w
		w-=1	
	print total1 + total2 - total3