## Problem 32

## We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, 
## the 5-digit number, 15234, is 1 through 5 pandigital.

## The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

## Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
## HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.


# define function
def pandg():
    
    # import timeit and start timer to measure time of function
    import timeit
    start = timeit.default_timer()
    
    list = [] # initialize list to hold all multiplicand, multiplier, and product
    solution = [] # initialize list for solution total
    
    for i in range(1,5000):
        
        for j in range(1,5000):
        
            if i*j < 10000:
                             
                if sorted(str(i) + str(j) + str(i*j)) == ['1','2','3','4','5','6','7','8','9']:
            
                    list.append(((str(i)+str(j)+str(i*j)),i*j))
    
    for k in range(0,len(list)):
    
        solution.append(list[k][1])
        
    print sum(set(solution))
    
    # stop timer and print total elapsed time
    stop = timeit.default_timer()
    print "Total time:", stop - start, "seconds"