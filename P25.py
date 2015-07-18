## Problem 25  

## The Fibonacci sequence is defined by the recurrence relation:

##    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

## Hence the first 12 terms will be:

##    F1 = 1
##    F2 = 1
##    F3 = 2
##    F4 = 3
##    F5 = 5
##    F6 = 8
##    F7 = 13
##    F8 = 21
##    F9 = 34
##    F10 = 55
##    F11 = 89
##    F12 = 144

## The 12th term, F12, is the first term to contain three digits.

## What is the index of the first term in the Fibonacci sequence to 
## contain 1000 digits?

# define function to find first fibonnaci # with 1000 digits    
def fib():
    
    # import timeit and start timer to measure time of function
    import timeit
    start = timeit.default_timer()
    
    # initialize variables to hold fibonacci # iterations and indx to hold index of largest fibonacci # F1
    F = 1 # for current fibonacci #
    F1 = 1 # for previous fibonacci #
    F2 = 1 # for lagging fibonacci #
    indx = 2
    
    # iterate through fibonacci #s while the length of latest fibonacci # is less than 1000
    while len(str(F1)) < 1000:
        
        F = F1 + F2 # generate new fibonacci number and store in F
        
        F2 = F1 # generate F2 (lagging fibonacci #) for next fibonacci number iteration
        
        F1 = F # generate F1 (previous fibonacci #) for next fibonacci number iteration     
        
        indx += 1 # iterate index value
    
    # print solution
    print indx
    
    # stop timer and print total elapsed time
    stop = timeit.default_timer()
    print "Total time:", stop - start, "seconds" 