## Problem 26   

## A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

##    1/2	= 	0.5
##    1/3	= 	0.(3)
##    1/4	= 	0.25
##    1/5	= 	0.2
##    1/6	= 	0.1(6)
##    1/7	= 	0.(142857)
##    1/8	= 	0.125
##    1/9	= 	0.(1)
##    1/10	= 	0.1

## Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

## Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

# re-used and modified code from problem 7 for generation of primes
def is_Prime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    if n%5==0: return False
    for i in range(3,int(n**0.5)+1,2):   # checks up to square root and only for odd numbers
        if n%i==0:
            return False    

        return True

# re-used and modified code from problem 7 for generation of primes    
def findprime():
    n = 4
    list = [7] # normally includes 2 and 3 here as initial prime numbers, however these were removed as 3 does not have recurring cycles > 1-digit and 2 has no recurring cycle
    while n < 1000: # checks for total number of prime numbers in list to continue iterations  
        if is_Prime(n):      # uses function above to check primality
            list.append(n)   # if number is prime, appends to list for tracking # of prime numbers computed
            n = n + 1        # iterates up
        else:
            n = n + 1        # iterates up but does not append # if not prime
    return list	

# define function   
def rep_cyc():
    
    # import timeit and start timer to measure time of function
    import timeit
    start = timeit.default_timer()
    
    # list of all primes less than 1000 per problem question 
    list = findprime()
    
    # list to hold length of each recurring cycle produced below
    solution_list = []
        
    # code to count length of each recurring cycle
    for i in list:
        
        #initialize integer for testing of each decimal place in each number
        j = 10
        
        # initialize count variable to count length of each recurring cycle
        count = 1
        
        # iterates until end of recurring cycle
        while j % i > 1:
    
            j = (j % i)*10 # tests remainder of each decimal place - when remainder gets to one again for each number tested, this indicates the cycle has ended
        
            count += 1 # iterate count of digits in recurring cycle 
           
        solution_list.append(count) # append count of digits in recurring cycle to solution_list
    
    # prints number in list of primes for index of max number in solution_list indicating largest recurring cycle
    print list[solution_list.index(max(solution_list))]
    
    # stop timer and print total elapsed time
    stop = timeit.default_timer()
    print "Total time:", stop - start, "seconds" 