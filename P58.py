## Problem 58

## Starting with 1 and spiralling anticlockwise in the following way, 
## a square spiral with side length 7 is formed.

## 37 36 35 34 33 32 31
## 38 17 16 15 14 13 30
## 39 18  5  4  3 12 29
## 40 19  6  1  2 11 28
## 41 20  7  8  9 10 27
## 42 21 22 23 24 25 26
## 43 44 45 46 47 48 49

## It is interesting to note that the odd squares lie along the bottom right diagonal, 
## but what is more interesting is that 8 out of the 13 numbers lying along both 
## diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

## If one complete new layer is wrapped around the spiral above, 
## a square spiral with side length 9 will be formed. If this process is continued, 
## what is the side length of the square spiral for which the ratio of primes along 
## both diagonals first falls below 10%?

# base function for problem 58
def spiral_primes():

	# import timeit and start timer to measure time of function
	import timeit
	start = timeit.default_timer()

	n=5 # starting digit in spiral is 5 (already counted 3 in prime_count below)
	
	iterator = int(round(n**.5-.5)) # amount to add to n for first diagonal
	
	iterator_count = 2 # counter to iterate through diagonals - four decreases each time before iterator changes - but starting at 5 so start at 2 here
	
	denominator = 3 # amount to divide total number of primes on diagonals by - to iterate one each check - starting with "1,3,5" so denominator begins at 3
	
	prime_count = 1 # initialize prime count integer
	
	while prime_count / float(denominator) >= .1: # iterate through diagonal numbers while >= 10%
	
		if is_Prime(n): # check primality of diagonal number
		
			prime_count += 1 # iterate prime count if number is prime
			
		iterator_count -= 1 # iterate counter down		
		
		n += iterator # iterate down to next diagonal number			
		
		if iterator_count == 0: # when iterator_count gets to 0
			
			iterator += 2 # iterator iterates down
			
			iterator_count = 4 # iterator_count is restored to 4
	
		denominator += 1
	
	# stop timer and print total elapsed time
	stop = timeit.default_timer()
	print "Total time:", stop - start
	
	return (denominator+1) / 2 # return length of side
	
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