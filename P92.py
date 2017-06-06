## Problem 92

## A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

## For example,

## 44 → 32 → 13 → 10 → 1 → 1
## 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

## Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will 
## eventually arrive at 1 or 89.

## How many starting numbers below ten million will arrive at 89?

# base function for problem 92
def number_chain():

	# import timeit and start timer to measure time of function
	import timeit
	start = timeit.default_timer()
	
	count = 0 # initialize count variable
	
	for i in range(2,999): # check starting numbers below ten million
		
		k = 0
		
		while k != 1 and k != 89:
		
			for j in range(0,len(str(i))-1):
			
				k += int(str(i)[j])**2

		if k == 89:

			count += 1
	
	# stop timer and print total elapsed time
	stop = timeit.default_timer()
	print "Total time:", stop - start
	
	return count