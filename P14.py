## Problem 14

## The following iterative sequence is defined for the set of positive integers:

## n → n/2 (n is even)
## n → 3n + 1 (n is odd)

## Using the rule above and starting with 13, we generate the following sequence:
## 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

## It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

## Which starting number, under one million, produces the longest chain?

## NOTE: Once the chain starts the terms are allowed to go above one million.

## Code below - note code is highly inefficient and took 253 seconds to find solution
## This was the first problem for which I clocked the processing time

def collatz():
    
    import timeit # imports timeit package for processing time stats
    start = timeit.default_timer() # starts timing program
    
    chain_list = [] # define list variable
       
    for n in range(999999,0,-1): # define range for iteration beginning with 999,999 per problem
        list = [n] # define list variable and set first value to number 
        while 1 not in list: # iterates through collatz sequence until sequence reaches 1
            if n % 2 == 0: # if number in sequence is even, divide by two and carry on
                n = n / 2
                list.append(n) # appends new number to list variable
            else:
                n = n*3 + 1 # if number in sequence is odd, multiply by three and add one and carry on
                list.append(n) # appends new number to list variable
        
		chain_list.append((len(list),list[0])) # appends a tuple for (# of links in chain, number)
        
	print max(chain_list) # prints max value in form (# of links in chain, number)
    
    stop = timeit.default_timer() # stops timing program
    print "Total time:", stop - start # prints elapsed seconds 