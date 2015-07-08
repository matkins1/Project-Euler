## Problem 21

## Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
## If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

## For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
## The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

## Evaluate the sum of all the amicable numbers under 10000.

# define function
def amicable():
    
    # import timeit and start timer to measure time of function
    import timeit
    start = timeit.default_timer()
     
    # initialize list for holding tuples for 1) each number 1 through 10,000 and 2) sum of factors of that number & other storage lists
    list = [] 
    factor_sum = []
    pair_list = []
    
    # iterate through range 10,000
    for i in range(1,10001):
        
        # clear factor_sum list for storage of factors of next iterable number
        factor_sum = []
        
        # test for factors of each number in range above
        for j in range(1,i):
            if i % j == 0:
                # if factor is found, store factor in list
                factor_sum.append(j)
        
        # appends tuple of (each successive digit in 10,000 range, sum of all factors of that digit)
        list.append((i,sum(factor_sum)))
        
    # code to iterate through "list" and check for amicable pairs and store those pairs in "pair_list" for evaluation below
    for k in range(0,10000):
        
        for l in range(0,10000):
        
            if list[l][1] == list[k][0] and list[l][0] == list[k][1] and k != l:
            
                pair_list.append(list[k][0])        
    
    # returns solution                
    print sum(pair_list)
    
    # stop timer and print total elapsed time
    stop = timeit.default_timer()
    print "Total time:", stop - start, "seconds" 