## Problem 48

## The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

## Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

# function to last ten digits in self power series
def self_Power():

	import timeit # import timeit and start timer to measure time of function
	start = timeit.default_timer()
	
	i = 1 # initialize integer for iterating
	solution = 0 # initialize solution variable
	
	while i < 1001:
	
		solution += i**i # append sum of self power to solution
		i += 1 # iterate
	
	print str(solution)[-10], str(solution)[-9], str(solution)[-8], str(solution)[-7], str(solution)[-6], str(solution)[-5], str(solution)[-4], str(solution)[-3], str(solution)[-2], str(solution)[-1]
	
	# stop timer and print total elapsed time
	stop = timeit.default_timer()
	print "Total time:", stop - start