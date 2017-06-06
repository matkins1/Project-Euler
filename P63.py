## Problem 63

## The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

## How many n-digit positive integers exist which are also an nth power?

# base function for problem 63
def dig_count():

	# import timeit and start timer to measure time of function
	import timeit
	start = timeit.default_timer()

	list = [] # initiate list
	
	for i in range(1,10): # 10 is upper bound on power - greater than 10 as power will cause resulting integer to be j + 1
	
		for j in range(1,999): # check up to arbitrary high end of range for power

			if len(str(i**j)) == j:

				list.append(i**j)
	
	# stop timer and print total elapsed time
	stop = timeit.default_timer()
	print "Total time:", stop - start
	
	return len(list)