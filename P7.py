# Project Euler Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# Personal notes
# Researched better code to check for primality per below (discovering only need to check up to square root of any given number
# for primarily along with obvious need to only check odd numbers above 2), then implemented a second function to store & 
# iterate prime numbers up to 10,001st prime number. 

# Code below

def is_Prime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # checks upt to square root and only for odd numbers
        if n%i==0:
            return False    

    return True

def findprime():
	n = 4
	list = [2, 3]
	while len(list) < 10001: # checks for total number of prime numbers in list to continue iterations  
		if is_Prime(n):      # uses function above to check primality
			list.append(n)   # if number is prime, appends to list for tracking # of prime numbers computed
			n = n + 1        # iterates up
		else:
			n = n + 1        # iterates up but does not append # if not prime
	print n	- 1		