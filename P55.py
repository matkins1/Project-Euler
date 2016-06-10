## Problem 55

## If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

## Not all numbers produce palindromes so quickly. For example,

## 349 + 943 = 1292,
## 1292 + 2921 = 4213
## 4213 + 3124 = 7337

## That is, 349 took three iterations to arrive at a palindrome.

## Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. 
## A number that never forms a palindrome through the reverse and add process is called a Lychrel number. 
## Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. 
## In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, 
## or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. 
## In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 
## 4668731596684224866951378664 (53 iterations, 28-digits).

## Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

## How many Lychrel numbers are there below ten-thousand?

## NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.

def lychrel():

	# import timeit and start timer to measure time of function
	import timeit
	start = timeit.default_timer()
	
	solution = [] # initialize list to hold all lychrel numbers
	
	for i in range(1,10000): # check numbers up to 10,000
		
		iterator = 0 # initialize iterator to iterate up to 50
		
		j = i # initialize integer to check for palindromic-ness
		x = i # lychrel number to append 
		
		while iterator < 50: # iterate up to 50 times per problem
			
			if pal(i + int(str(j)[::-1])): # check if reverse and add is palindromic
				iterator = 99 # iterator to 100
			
			iterator += 1 # iterate up to 50
			
			j = i + int(str(i)[::-1]) # j equals reverse and add of i
			i = j # i equals j
	
		if iterator != 100: # if number before 50 iterations was not palindromic (was lychrel)
			solution.append(x) # append number if lychrel 
	
	print len(solution) # return solution

	# stop timer and print total elapsed time
	stop = timeit.default_timer()
	print "Total time:", stop - start
	
# function to test if number is palindromic    
def pal(n): # define function
	n = str(n) # convert number to string
	return n == n[::-1] # return "True" if string of "n" equals the reverse of string of "n"   	