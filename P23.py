## Problem 23

## A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
## For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

## A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

## As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
## By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
## However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be 
## expressed as the sum of two abundant numbers is less than this limit.

## Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

# define function for creating list tuples of (numbers, sum of factors)
def factors():

    # initialize list for holding tuples for 1) each number 1 through 28,123 and 2) sum of factors of that number & other storage lists
    list = [] 
    temp_list = []
    
    # iterate through range 14,061 (half of 28,123 amount above as we are looking at sums of two abundant numbers)
    for i in range(1,28124):
        
        # clear temp_list for storage of factors of next iteration
        temp_list = []
        
        # test for factors of each number in range above
        for j in range(1,i):
            
            if i % j == 0:
                
                # if factor is found, store factor in list
                temp_list.append(j)
        
        # appends tuple of (each successive digit in 28,123 range, sum of all factors of that digit)
        list.append((i,sum(temp_list)))
    
    # returns list of tuples (number, sum of factors)
    return list

# define function for returning list of abundant numbers using factors() function
def return_abundant():
    
    # calls factors() function and stores results in list
    list = factors()
    
    #initialize list to hold all abundant numbers
    abundant_list = []
       
    # code to iterate through "list" and check for abundant numbers pairs in list and store those numbers in "abundant_list"
    for k in range(0,len(list)):
        
        if list[k][1] > list[k][0]:
            
            abundant_list.append(list[k][0])

    # returns list of all abundant numbers
    return abundant_list
    
# define function to generate all sums of two abundant numbers from list of abundant numbers using factors() and return_abundant() functions
def check_abundant():
    
    # import timeit and start timer to measure time of function
    import timeit
    start = timeit.default_timer()
    
    import itertools
    
    # calls return_abundant() function and stores results in list
    list = return_abundant()
    abundant_sums = []
    
    # iterate through list and generate sums of all numbers
    for l in range(0,len(list)):
        
        for m in range((l-1),len(list)):
        
            abundant_sums.append(list[l] + list[m])
    
    # sort and remove duplicates
    abundant_sums = sorted(set(abundant_sums))
    
    # remove all sums over 28123
    abundant_sums = filter(lambda a: a < 28124, abundant_sums)
    
    # returns solution which is sum of all positive integers through 28,123 less sum of integers that can be made with abundant sums
    print (sum(range(0,28124)) - sum(abundant_sums))

    # stop timer and print total elapsed time
    stop = timeit.default_timer()
    print "Total time:", stop - start, "seconds"