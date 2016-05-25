## Problem 50

## The prime 41, can be written as the sum of six consecutive primes:
## 41 = 2 + 3 + 5 + 7 + 11 + 13

## This is the longest sum of consecutive primes that adds to a prime below one-hundred.

## The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

## Which prime, below one-million, can be written as the sum of the most consecutive primes?

### Notes: We know that the solution is a prime below a million and the floor on the number of terms is 21 per the problem so 
### the max number we need to check up to is 45,454 (1,000,000/22). The ceiling on the number of terms is 546, beginning from 2 up to 3,391 totaling 997,661 (not prime though).
### Planning on starting with 546 terms and checking downward.

def prime_Sum():

	import timeit # import timeit and start timer to measure time of function
	start = timeit.default_timer()
	
	prime_list = [] # initialize list to hold all primes
	
	for i in range(2,45454): # compile list prime numbers for summing
	
		if is_Prime(i): # if number is prime

			prime_list.append(i) # append number to prime_list
	
	for k in range (546,21,-1): # try highest potential number of terms and decrease
	
		for j in prime_list: # iterate up each term in prime list
	
			floor = prime_list.index(j) # define starting point as index in prime list
	
			if is_Prime(sum(prime_list[floor:k])): # since iterating down from highest potential number of terms, return first prime number generated from prime sums
	
				print sum(prime_list[floor:k]) 
				
				break			
			
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