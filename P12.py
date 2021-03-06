## The sequence of triangle numbers is generated by adding the natural numbers. 
## So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. 
## The first ten terms would be:

## 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

## Let us list the factors of the first seven triangle numbers:

##      1: 1
##      3: 1,3
##      6: 1,2,3,6
##     10: 1,2,5,10
##     15: 1,3,5,15
##     21: 1,3,7,21
##     28: 1,2,4,7,14,28

## We can see that 28 is the first triangle number to have over five divisors.

## What is the value of the first triangle number to have over five hundred divisors?

## Code below

# factors function to find all factors for triangle numbers
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

# function to create triangle numbers and use factors function above to decompose into factors				
def tri_div():
	x = [1]
	y = 2
	while len(factors(sum(x))) < 501: # checks if variable x has over 500 factors
		x.append(y)
		y += 1
	return sum(x) # returns solution to problem