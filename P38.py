## Problem 38

## Take the number 192 and multiply it by each of 1, 2, and 3:

##    192 × 1 = 192
##    192 × 2 = 384
##    192 × 3 = 576

## By concatenating each product we get the 1 to 9 pandigital, 192384576. 
## We will call 192384576 the concatenated product of 192 and (1,2,3)

## The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, 
## giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

## What is the largest 1 to 9 pandigital 9-digit number that can be formed as 
## the concatenated product of an integer with (1,2, ... , n) where n > 1?

# Notes: Only need to check certain combinations...9999-5000 for (1,2), 333-100 for (1,2,3),
# 33-25 for (1,2,3,4), 9-5 for (1,2,3,4,5) as results outside these combinations are larger
# or smaller than 9-digits

# function to find pandigital multiples
def pan():
	
	# import timeit and start timer to measure time of function
	import timeit
	start = timeit.default_timer()	
	
	list = [] # initialize list to hold all potential pandigitals
	solution = [] # initalize solution
	
	n = 9999 # initalize count for first set - 9999-5000 for (1,2)
	
	while n > 4999: # test first set
	
		list.append(str(n*1) + str(n*2)) # append potential pandigital
		n -= 1 # reduce n
	
	n = 333 # initalize count for second set - 333-100 for (1,2,3)
	
	while n > 99: # test second set
	
		list.append(str(n*1) + str(n*2) + str(n*3)) # append potential pandigital
		n -= 1 # reduce n	
	
	n = 33 # initalize count for third set - 33-25 for (1,2,3,4)
	
	while n > 24: # test third set
	
		list.append(str(n*1) + str(n*2) + str(n*3) + str(n*4)) # append potential pandigital
		n -= 1 # reduce n		
		
	n = 9 # initalize count for fourth set - 9-5 for (1,2,3,4,5)
	
	while n > 4: # test fourth set
	
		list.append(str(n*1) + str(n*2) + str(n*3) + str(n*4) + str(n*5)) # append potential pandigital
		n -= 1 # reduce n		
	
	for i in list: # iterate through list and check all for pandigital-ness
		
		if isPandigital(int(i)): # check if item is pandigital
		
			solution.append(i) # add element of list to solution if pandigital
	
	solution.sort(reverse=True) # sort list of pandigitals for largest
	
	print solution[0] # print solution
	
	# stop timer and print total elapsed time
	stop = timeit.default_timer()
	print "Total time:", stop - start, "seconds"

# function to check for pandigital-ness
def isPandigital(n):
	if "0" in str(n): return False # eliminate pandigital #s including "0" since this code is used to
	# search for 9-digit pandigital #s and therefore must excluded "0"
	# (includes "1" through "9")
	count = 10*[0]
	while n != 0:
		if count[n%10] == 1: return False
		count[n%10] += 1
		n /= 10
	return True	