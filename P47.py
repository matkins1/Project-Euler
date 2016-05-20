## Problem 47

## The first two consecutive numbers to have two distinct prime factors are:

## 14 = 2 × 7
## 15 = 3 × 5

## The first three consecutive numbers to have three distinct prime factors are:

## 644 = 2^2 × 7 × 23
## 645 = 3 × 5 × 43
## 646 = 2 × 17 × 19.

## Find the first four consecutive integers to have four distinct prime factors. 
## What is the first of these numbers?

# function to find first of four consecutive integers to have four distinct prime factors
def fp_Factors():

	import timeit # import timeit and start timer to measure time of function
	start = timeit.default_timer()
	
	solution = [0,0,0,0] # initialize solution list
	
	integers = 2 # initialize integers for iteration
	
	while (solution[-1] - solution[-2] + solution[-3] - solution[-4]) != 2 or (solution[-2] - solution[-3]) != 1: # loop while solution is not found
	
		if len(set((prime_factors(integers)))) == 4: # check if integer has four unique prime factors
		
			solution.append(integers) # append integer to solution
			
		integers += 1 # iterate integers	
	
	print solution[-4], solution[-3], solution[-2], solution[-1] # print four consecutive integers
	
	# stop timer and print total elapsed time
	stop = timeit.default_timer()
	print "Total time:", stop - start

# function to find prime factors
def prime_factors(n):
    i = 2 
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors