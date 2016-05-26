## Problem 52

## It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

## Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

def perm_mult():

	import timeit # import timeit and start timer to measure time of function
	start = timeit.default_timer()
	
	integer = 1 # initialize integer to iterate
	
	# check for condition given in problem and iterate integers if condition is not present
	while set(str(integer)) != set(str(integer*2)) or set(str(integer*2)) != set(str(integer*3)) \
		or set(str(integer*3)) != set(str(integer*4)) or set(str(integer*4)) != set(str(integer*5)) \
		or set(str(integer*5)) != set(str(integer*6)):
	
		integer += 1 # iterate
	
	print integer # print solution
	
	# stop timer and print total elapsed time
	stop = timeit.default_timer()
	print "Total time:", stop - start
