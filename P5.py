# Project Euler Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

## Created brute force code below in short amount of time, then realized that checks between 1 & 10 could be eliminated to double efficiency
## Note there's probably an even more efficient way to code this but the final code took ~10 seconds to run

## def check():
##	n = 1

##	while (n%1 != 0) or (n%2 != 0) or (n%3 != 0) or (n%4 != 0) or (n%5 != 0) or (n%6 != 0) or (n%7 != 0) or (n%8 != 0) or (n%9 != 0) or (n%10 != 0) or (n%11 != 0) or (n%12 != 0) or (n%13 != 0) or (n%14 != 0) or (n%15 != 0) or (n%16 != 0) or (n%17 != 0) or (n%18 != 0) or (n%19 != 0) or (n%20 != 0):    
##		n = n + 1  
##	print n			

### Final more efficient code below

def check():
	n = 1

	while (n%11 != 0) or (n%12 != 0) or (n%13 != 0) or (n%14 != 0) or (n%15 != 0) or (n%16 != 0) or (n%17 != 0) or (n%18 != 0) or (n%19 != 0) or (n%20 != 0):    
		n = n + 1  
	print n			
