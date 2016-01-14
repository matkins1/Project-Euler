## Problem 41

## We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
## For example, 2143 is a 4-digit pandigital and is also prime.

## What is the largest n-digit pandigital prime that exists?

# Note: upper limit on pandigital number that is prime is 7-digit 7654321 since 8 & 9-digit pandigital numbers are all divisible by 3 and thus cannot be prime

# function to find largest pandigital prime
def pan_Prime():

	# import timeit and start timer to measure time of function
	import timeit
	start = timeit.default_timer()	

	for i in xrange(7654321,2,-1):
	
		if is_Pandigital(i) and is_Prime(i): # check primaliy and pandigitalness
			
			print i
			
			break
	
	# stop timer and print total elapsed time
	stop = timeit.default_timer()
	print "Total time:", stop - start, "seconds"		
	
# function for determination of primality    
def is_Prime(n):
    if n < 2: # returns false if number is less than 2
        return False
    if n == 2: # returns true if number is 2
       return True
    if n % 2 == 0: # returns true if number is even
        return False    
    i = 3 # iterates through all possible divisors of number up to the square root of that number and returns true if not divisible by any number
    while i <= n**.5:
        if n % i == 0:
            return False
        i = i+2
    return True 	

# function for determination of pandigitalness    
def is_Pandigital(n):
	if "0" in str(n): return False # eliminate pandigital #s including "0" per problem question
	if "9" in str(n): return False # eliminate pandigital #s including "9" as 9 & 8 digit pandigitals cannot be prime
	if "8" in str(n): return False # eliminate pandigital #s including "8" as 9 & 8 digit pandigitals cannot be prime
	count = 10*[0]
	while n != 0:
		if count[n%10] == 1: return False
		count[n%10] += 1
		n /= 10
	return True		