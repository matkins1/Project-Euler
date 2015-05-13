# Project Euler Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

# Personal Notes
# Researched Sieve of Eratosthenes for determining primes, Miller-Rabin primality test
# for determining primes, and ways to find prime factors of numbers in Python

# Code below

n = 600851475143; i = 2

while i * i < n:    ## top level while loop terminates for highest possible i below n
    while n%i == 0: ## checks if i is a prime factor of n and sets n = to n / prime factor
        n = n / i   
    i = i + 1       ## iterates i + 1 until n%i = 0

print (n)			## prints largest prime factor of original n