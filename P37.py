## Problem 37

## The number 3797 has an interesting property. Being prime itself, it is possible to 
## continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. 
## Similarly we can work from right to left: 3797, 379, 37, and 3.

## Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

## NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

# function to find whether primes are truncatable
def trunc_prime(n):
	
	# import timeit and start timer to measure time of function
	import timeit
	start = timeit.default_timer()
    
	solution = [] # initialize solution list to hold eleven primes
	
	list = prime_list(n) # store list of primes

	for i in list: # iterate through list of primes

		con = 1 # initialize counter
		
		z = str(i) # initialize string value of each i iteration
		
		bo = True # initialize bool for testing of prime iterations
		bo1 = True # initialize bool for testing of prime iterations
	
		while con < len(z) and bo == True and bo1 == True: # iterate and check primality of each truncatable  

			bo = is_Prime(int(z[con:])) # check each truncation
		
			bo1 = is_Prime(int(z[:-con])) # check each truncation 
			
			con += 1	# iterate count
		
		if bo == True and bo1 == True:

			solution.append(i) # append prime number to solution list if boolean value remains true
			
	print solution # print solution list
	print sum(solution) # print sum of solution list for answer
	
	# stop timer and print total elapsed time
	stop = timeit.default_timer()
	print "Total time:", stop - start, "seconds"

# function to generate list of primes less than n 
def prime_list(n):      
    list2 = [] # initialize list
    
    for i in range(11,n): # iterates through all numbers in range - starts at 11 since primes below 11 are non-truncatable per problem
                   
        if is_Prime(i): # checks if number in range is prime
        
            list2.append(i) # appends number to list if prime
            
    return list2 # returns list of prime numbers
    
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
