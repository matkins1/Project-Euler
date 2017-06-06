## Problem 51

## By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

##By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, 
## yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with 
## this property.

## Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

# base function for problem 51
def prime_replacement():

	# import timeit and start timer to measure time of function
	import timeit
	start = timeit.default_timer()

	
	
	
	# stop timer and print total elapsed time
	stop = timeit.default_timer()
	print "Total time:", stop - start

# function to generate primes
def prime_numbers():

	prime_list = [] # initialize list

	for i in range (2,1000000): # generate primes up to 1,000,000 arbitrary amount

		if is_Prime(i): # append prime number to list
			
			prime_list.append(i) 
	
	return prime_list
	
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