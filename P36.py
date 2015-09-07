## Problem 36

## The decimal number, 585 = 1001001001^2 (binary), is palindromic in both bases.

## Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

## (Please note that the palindromic number, in either base, may not include leading zeros.)

def both_pal():
    
    # import timeit and start timer to measure time of function
    import timeit
    start = timeit.default_timer()
    
    sum_total = 0 # initialize sum_total variable to hold sum of all palindromic numbers
    
    for i in range(1,1000000): # check all number less than one million per question
    
        if pal(i) and pal(int(bin(i)[2:])): # check palindrome condition for number in base 10 and base 2
        
            sum_total += i # add palindromic number to sum_total
       
    print sum_total # print answer
    
    # stop timer and print total elapsed time
    stop = timeit.default_timer()
    print "Total time:", stop - start, "seconds"

# function to test if number is palindromic    
def pal(n): # define function
	n = str(n) # convert number to string
	return n == n[::-1] # return "True" if string of "n" equals the reverse of string of "n"    