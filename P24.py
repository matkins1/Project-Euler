## Problem 24  

## A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
## If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
## The lexicographic permutations of 0, 1 and 2 are:

## 012   021   102   120   201   210

## What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

### Personal Note - thought about problem and realized can generate 1,000,000th sequence by using factorial
### values of length of list instead of attempting to sort list lexicographically 

# define function to return millionth lexicographic permutation of digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9    
def lex_perm():

    # import timeit and start timer to measure time of function
    import timeit
    start = timeit.default_timer()

    # import math package for factorial function
    import math
    
    # initiate variables
    list = [0,1,2,3,4,5,6,7,8,9] # list of all digits from problem
    solution = [] # list to hold solution (popped from list variable)
    holding = 0 # variable to hold each increment of solution
    holding1 = 0 # variable to hold amount to increment seq variable
    seq = 1000000 # sequence variable to iterate down to 0
    perm_len = 0 # variable to iterate through position in list
    
    # iterate until sequent variable == 0
    while seq > 4: # stopped at 4 since that gives 4 permutations left with digits 0,4,6 remaining. code at end to sort fourt permutation of these final digits.
        
        # set holding variables == 0
        holding = 0
        holding1 = 0
        
        # iterate through digits place if remaining combos greater than sequence length
        if math.factorial(len(list)-perm_len) > seq:
            
            # iterate digits place
            perm_len += 1
                    
        # add digit to solution and remove from list for next iteration
        else:
            holding1 = (seq / math.factorial(len(list)-perm_len))
            holding = list.pop(seq / math.factorial(len(list)-perm_len))      
            
            # reduce sequence variable by factorial times digit popped above
            seq -= math.factorial(len(list)-perm_len+1) * holding1
            
            # append digit to solution
            solution.append(holding)
    
    ## sequent to re-arrange last three digits lexicographically
    seq -= 1
    
    list[0], list[1], list[2] = list[0], list[2], list[1]
    seq -= 1
    
    list[0], list[1], list[2] = list[2], list[0], list[1]
    seq -= 1
    
    list[0], list[1], list[2] = list[0], list[2], list[1]
    seq -= 1
    
    #list[0], list[1], list[2] = list[1], list[2], list[0]
    #list[0], list[1], list[2] = list[0], list[2], list[1]
    
    # append final three digits in list to solution
    for i in list:
        solution.append(i)
    
    # print solution
    print solution

    # stop timer and print total elapsed time
    stop = timeit.default_timer()
    print "Total time:", stop - start, "seconds"