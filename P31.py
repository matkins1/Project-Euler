## Problem 31

## In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

##     1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

## It is possible to make £2 in the following way:

##     1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

## How many different ways can £2 be made using any number of coins?

# define function
def coin_sum():
    
    # import timeit and start timer to measure time of function
    import timeit
    start = timeit.default_timer()
    
    ways = [0]*201

    ways[0] = 1
    
    for x in [1,2,5,10,20,50,100,200]:
    
        for i in xrange(x, 201):
            
            ways[i] += ways[i-x]
    
    print ways[200]
            
    # stop timer and print total elapsed time
    stop = timeit.default_timer()
    print "Total time:", stop - start, "seconds"