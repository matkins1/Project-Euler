## Problem 20

## n! means n × (n − 1) × ... × 3 × 2 × 1

## For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
## and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

## Find the sum of the digits in the number 100!

## Code below

# define function
def sum_dig():
    
    # import timeit and start timer to measure time of function
    import timeit
    start = timeit.default_timer()
    
    # import math package for truncate function use
    import math 
    
    prod = 1 # initialize variable for product of n! 
    
    dig_sum = [] # initialize variable for sum of digits
    
    for i in range(100,0,-1): # iterate through 100 backwards
	
        prod = prod * i # stores product of each successive iteration for n!

    math.trunc(prod) # truncate long integer (remove 0s)
    
    prod = str(prod) # converts prod to string type    
   
    for j in prod: # iterate through each digit in "prod"
        
        dig_sum.append(int(j)) # add each digit to list for summation 
        
    print sum(dig_sum) # returns sum of digits
        
    # stop timer and print total elapsed time
    stop = timeit.default_timer()
    print "Total time:", stop - start, "seconds" 