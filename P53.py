## Problem 53

## There are exactly ten ways of selecting three from five, 12345:

## 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

## In combinatorics, we use the notation, 5C3 = 10.

## In general,
## nCr = 	
## n!
## r!(n−r)!
## 	 ,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

## It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

## How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?

def comb_select():

	import timeit # import timeit and start timer to measure time of function
	start = timeit.default_timer()
	
	import math # import math package for factorial function
	
	solution = [] # initialize solution list
	
	for n in range(1,101): # iterate through range 1 ≤ n ≤ 100
		
		for r in range(1,n): # iterate through range 1 ≤ n
		
			if math.factorial(n) / (math.factorial(r)*math.factorial(n-r)) > 1000000: # check if combinatorial selection total > 1000000
			
				solution.append(math.factorial(n) / (math.factorial(r)*math.factorial(n-r))) # append combinatorial selection total if above condition met
	
	print len(solution) # return solution
	
	# stop timer and print total elapsed time
	stop = timeit.default_timer()
	print "Total time:", stop - start