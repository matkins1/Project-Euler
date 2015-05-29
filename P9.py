# Project Euler Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a**2 + b**2 = c**2

# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

## Personal notes 
## Researched Euclid's formula for generating Pythagorean triples but used brute force approach below given quickness of algorithm

# Code below
		
def py_trip(): # define function
	a = 1; b = 1; c = 1 # define variables
	for i in range(2,1000): # first loop iterates b after all combos of a
		for j in range(2,1000): # second nested loop iterates a
			c = a**2 + b**2 # stores c**2 variable in c
			if a**2 + b**2 == c and a + b + c**.5 == 1000: # checks condition of problem and returns answer and breaks loop if found (had to use sqrt on c since it is stored as c**2)
				print a * b * c**.5 # prints answer
				print a, b, c**.5  # prints components of answer
				break # breaks loop
			a = j # iterate a	
		b = i # iterate b after all combos of a
		a = 1 # set a back to 1	