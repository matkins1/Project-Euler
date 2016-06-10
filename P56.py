## Problem 56

## A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: 
## one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

## Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?


def pow_dig():

	# import timeit and start timer to measure time of function
	import timeit
	start = timeit.default_timer()
	
	solution = 0 # initialize solution to hold maximum digital sum
	
	for a in range(1,101): # iterate a through 100 per problem
	
		for b in range(1,101): # iterate b through 100 per problem
		
			counter = 0 # initialize digital sum counter
		
			for i in str(a**b): # iterate through digits of a^b
			
				counter += int(i) # compute digital sum
				
			if counter > solution: # check if latest digital sum is larger than previously computed

				solution = counter # solution equals latest digital sum computed
			
	print solution # print solution			
	
	# stop timer and print total elapsed time
	stop = timeit.default_timer()
	print "Total time:", stop - start
