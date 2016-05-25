## Problem 49

## The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
## (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

## There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, 
## but there is one other 4-digit increasing sequence.

## What 12-digit number do you form by concatenating the three terms in this sequence?

def prime_Perm():

	import timeit # import timeit and start timer to measure time of function
	start = timeit.default_timer()
	
	prime_list = [] # initialize list to hold all primes
	
	for i in range(1000,10000): # compile list of 4-digit prime numbers
	
		if is_Prime(i): # if number is prime

			prime_list.append(i) # append number to prime_list
			
	for j in prime_list: # iterate and check two conditions for solution
	
		for k in prime_list:
		
				for m in prime_list:
				
					if (m - k) == (k - j) and sorted(str(j)) == sorted(str(k)) and sorted(str(k)) == sorted(str(m)) and j != k and k != m: # check for three numbers that are permutations of one another and that are in an arithmetic sequence
					
						print j, k, m
	
	# stop timer and print total elapsed time
	stop = timeit.default_timer()
	print "Total time:", stop - start
	
# function for determination of primality    
def is_Prime(n):
    if n < 2: # returns false if number is less than 2
        return False
    if n == 2: # returns true if number is 2
       return True
    if n % 2 == 0: # returns false if number is even
        return False    
    i = 3 # iterates through all possible divisors of number up to the square root of that number and returns true if not divisible by any number
    while i <= n**.5:
        if n % i == 0:
            return False
        i = i+2
    return True 		