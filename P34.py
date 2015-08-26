## Problem 34

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

def dig_fact():
    
    # import timeit and start timer to measure time of function
    import timeit
    start = timeit.default_timer()
    
    import math # import math package for factorial function
    
    sum_total = 0 # initialize sum variable to hold sum of digit factorials
    
    list = [] # initalize list to hold all numbers which are equal to the sum of the factorial of their digits
    
    for i in range(3,math.factorial(9)*7): # iterate through range and check conditions per problem
   
        sum_total = 0 # reset sum variable for each number in range above
   
        for j in range(0,len(str(i))): # iterate through each digit of number in range above
                
            sum_total += math.factorial(int(str(i)[j])) # add factorial of each digit of number to "sum" variable for checking problem condition below
            
        if i == sum_total: # append number to list if it is equal to the sum of the factorial of its digits
            
            list.append(i)
            
    print sum(list) # return solution        
            
    # stop timer and print total elapsed time
    stop = timeit.default_timer()
    print "Total time:", stop - start, "seconds"