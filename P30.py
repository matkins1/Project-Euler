## Problem 30

## Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

##     1634 = 1**4 + 6**4 + 3**4 + 4**4
##     8208 = 8**4 + 2**4 + 0**4 + 8**4
##     9474 = 9**4 + 4**4 + 7**4 + 4**4

## As 1 = 1**4 is not a sum it is not included.

## The sum of these numbers is 1634 + 8208 + 9474 = 19316.

## Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

# define function
def fifth_pow():
    
    # import timeit and start timer to measure time of function
    import timeit
    start = timeit.default_timer()
    
    # initialize list to hold sum of fifth powers of their digits in range below, and solution to hold answer
    list = []
    solution = []
    
    # iterate through presumed range of solutions - 7*9**5 yields a six digit number so six digits is presumed the upper boundary
    for i in range(0,(6*9**5)):
        
        a = 0 # integer to iterate through sum of all fifth powers of digits
        
        for j in str(i): # converts each number into string for iteration through digits
        
            a += int(j)**5 # sums all fifth powers of digits of each number

        list.append(a) # appends sum found above to list
	
    # checks if sum of fifth powers of digits equals number it was derived from
    for k in range(0,(6*9**5)):
        
        if k == list[k]:
    
            solution.append(k) # appends numbers to solution list
    
    print sum(solution) - 1 # prints sum of all numbers less one, as one is noted as being excluded per above
    
    # stop timer and print total elapsed time
    stop = timeit.default_timer()
    print "Total time:", stop - start, "seconds"   