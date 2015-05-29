# Project Euler Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# Personal notes
# Re-used code from problem 7 to find all prime numbers under two million and returned sum of numbers stored in list

# Code below

def is_Prime(n): # efficient function to test primality
    if n==2 or n==3: return True  # returns true if number is 2 or 3
    if n%2==0 or n<2: return False # returns false if number is even (easy check for efficiency to eliminate all even numbers) or less than 2
    for i in range(3,int(n**0.5)+1,2):   # checks odd numbers up to the square root of n 
        if n%i==0: 					     # if number is divisible by any integer returns false
            return False    

    return True							 # returns true if no conditions above are violated 

def prime_sum():
	n = 4
	list = [2, 3]
	while n < 2000000: # iterates while n is less than two million per problem text 
		if is_Prime(n):        # uses function above to check primality
			list.append(n)     # if number is prime, appends to list for tracking # of prime numbers computed
			n = n + 1          # iterates up
		else:
			n = n + 1          # iterates up but does not append # if not prime
	m = sum(list)			   # sums all values in list
	print m					   # prints sum of list