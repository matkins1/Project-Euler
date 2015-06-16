## Project 15

## Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

## How many such routes are there through a 20×20 grid?

## Personal notes - researched latice paths and combinations
## noting that the total # of paths from (0,0) to (20,20) is
## the solution of 40 choose 20 given binomial coefficient
## formula (n + k) ((n + k) choose n) where n,k is the end
##			  n
## point and 0,0 is the start point

## Code below

# initializes function
def choose(n, k): 
    
    # import timeit and start timer to measure time of function
    import timeit
    start = timeit.default_timer()
    
    # checks if inputs are in range
    if 0 <= k <= n: 
        ntok = 1 # initializes variables
        ktok = 1 # initializes variables
        
        # calculates and returns choose solution
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        
        print ntok // ktok
        
    # returns 0 if inputs are out of range
    else:		  
        print 0

    # stop timer and print total elapsed time
    stop = timeit.default_timer()
    print "Total time:", stop - start     
        
choose(40,20) # ((n + k) choose n))
    print "Total time:", stop - start # prints elapsed seconds 