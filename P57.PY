## Problem 57

## It is possible to show that the square root of two can be expressed as an infinite continued fraction.

## √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

## By expanding this for the first four iterations, we get:

## 1 + 1/2 = 3/2 = 1.5
## 1 + 1/(2 + 1/2) = 7/5 = 1.4
## 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
## 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

## The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, 
## is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

## In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?

### The fracts will be Pell number series defined as (Pn-1 + Pn) / Pn

def sqr_conv():

	# import timeit and start timer to measure time of function
	import timeit
	start = timeit.default_timer()
	
	num = 3 # define first numerator
	
	den = 2 # define first denominator
	
	hold_den = 2 # define holding denominator
	
	n = 1 # iterator through first 1000 expansions
	
	solution = 0 # initialize solution count
	
	while n < 1000: # first 1000 expansions per problem

		if len(str(num)) > len(str(den)): # numerator is larger than denominator
		
			solution += 1 # add to solution count
		
		n += 1 # iterate expansion count
		
		hold_den = den # reset holding denominator
		
		den = num + den # iterate denominator
		
		num = hold_den + den # iterate numerator
		
	print solution
	
	# stop timer and print total elapsed time
	stop = timeit.default_timer()
	print "Total time:", stop - start