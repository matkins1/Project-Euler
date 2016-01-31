## Problem 46

## It was proposed by Christian Goldbach that every odd composite number can be 
## written as the sum of a prime and twice a square.

## 9 = 7 + 2×1^2
## 15 = 7 + 2×2^2
## 21 = 3 + 2×3^2
## 25 = 7 + 2×3^2
## 27 = 19 + 2×2^2
## 33 = 31 + 2×1^2

## It turns out that the conjecture was false.

## What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

# function to find smallest odd composite that cannot be written as the sum of a prime and twice a square
def Goldbach():

	import timeit # import timeit and start timer to measure time of function
	start = timeit.default_timer()
	
	prime_list = [] # list to hold prime numbers
	composite_list = [] # list to hold potential composite numbers
	
	for i in range(1,10000): # generate list of prime numbers and add to prime_list - upper bound is arbitrary
		if is_Prime(i):
			prime_list.append(i)
	
	for j in prime_list: # generate list of composites made from numbers prime_list + 2*squares - upper bound is arbitrary
		for k in range(1,100):
			composite_list.append(j+(2*(k**2)))
	
	composite_list = sorted(composite_list, reverse=False) # sort list from smallest to largest
	
	for l in range(2,1000000):
		if l not in composite_list and l % 2 != 0 and not is_Prime(l):
			print l
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