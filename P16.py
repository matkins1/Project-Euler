## Problem 16

## 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

## What is the sum of the digits of the number 2**1000?

## Code below

# initialize function, where x is the power to raise by
def power_dig(x):

    # import timeit and start timer to measure time of function
    import timeit
    start = timeit.default_timer()

    # store power of 2 to x in variable "a" and initialize "list"
    a = str(2**x)
    list = []
    
    # iterate over length of 2**x and store each integer of solution in "list"    
    for i in range(0,len(a)):
        list.append(int(a[i]))
    
    # print sum of single integers in list from decomposed solution to 2**x
    print sum(list)
    
    # stop timer and print total elapsed time
    stop = timeit.default_timer()
    print "Total time:", stop - start 