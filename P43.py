## Problem 43

## The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of 
## the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

## Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

##    d2d3d4=406 is divisible by 2
##    d3d4d5=063 is divisible by 3
##    d4d5d6=635 is divisible by 5
##    d5d6d7=357 is divisible by 7
##    d6d7d8=572 is divisible by 11
##    d7d8d9=728 is divisible by 13
##    d8d9d10=289 is divisible by 17

## Find the sum of all 0 to 9 pandigital numbers with this property.

# function to find all pandigital numbers with unique substring properties
def sub_Pan():

	import timeit # import timeit and start timer to measure time of function
	start = timeit.default_timer()
	
	d17 = []; d13 = []; d11 = []; d7 = []; d5 = []; d3 = [] # initialize list to hold all divisors
	combinations = [] # initialize list to hold all potential combinations with noted sub-string divisibility properties per question
	solution = [] # initialize list to hold solution
	
	iterator = 1 # initialize iterator to generate all applicable divisors below
	while iterator*17 < 1000:
		if iterator*17 > 99 and is_Pandigital(iterator*17):
			d17.append(str(iterator*17))
		if iterator*17 < 100 and is_Pandigital(iterator*17):
			d17.append(str(0) + str(iterator*17))
		iterator += 1
		
	iterator = 1 # initialize iterator to generate all applicable divisors below
	while iterator*13 < 1000:
		if iterator*13 > 99 and is_Pandigital(iterator*13):
			d13.append(str(iterator*13))
		if iterator*13 < 100 and is_Pandigital(iterator*13):
			d13.append(str(0) + str(iterator*13))
		iterator += 1

	iterator = 1 # initialize iterator to generate all applicable divisors below
	while iterator*11 < 1000:
		if iterator*11 > 99 and is_Pandigital(iterator*11):
			d11.append(str(iterator*11))
		if iterator*11 < 100 and is_Pandigital(iterator*11):
			d11.append(str(0) + str(iterator*11))
		iterator += 1

	iterator = 1 # initialize iterator to generate all applicable divisors below
	while iterator*7 < 1000:
		if iterator*7 > 99 and is_Pandigital(iterator*7):
			d7.append(str(iterator*7))
		if iterator*7 < 100 and is_Pandigital(iterator*7):
			d7.append(str(0) + str(iterator*7))
		iterator += 1				
	
	iterator = 1 # initialize iterator to generate all applicable divisors below
	while iterator*5 < 1000:
		if iterator*5 > 99 and is_Pandigital(iterator*5):
			d5.append(str(iterator*5))
		if iterator*5 < 100 and is_Pandigital(iterator*5):
			d5.append(str(0) + str(iterator*5))
		iterator += 1		

	iterator = 1 # initialize iterator to generate all applicable divisors below
	while iterator*3 < 1000:
		if iterator*3 > 99 and is_Pandigital(iterator*3):
			d3.append(str(iterator*3))
		if iterator*3 < 100 and is_Pandigital(iterator*3):
			d3.append(str(0) + str(iterator*3))
		iterator += 1	

	for j in d13: # generate all possible solutions - ending four digits
		
		for i in d17:
		
			if i[0:2] == j[1:3] and is_Pandigital(int(str(j[0]+i))):	
		
				combinations.append(j[0]+i)

	d13 = combinations # transfer all potential ending four digits to d13 list
	combinations = [] # reset combinations list
	
	for j in d11: # generate all possible solutions - ending five digits
		
		for i in d13:
		
			if i[0:2] == j[1:3] and is_Pandigital(int(str(j[0]+i))):	
		
				combinations.append(j[0]+i)
	
	d11 = combinations # transfer all potential ending five digits to d11 list
	combinations = [] # reset combinations list
	
	for j in d7: # generate all possible solutions - ending six digits
		
		for i in d11:
		
			if i[0:2] == j[1:3] and is_Pandigital(int(str(j[0]+i))):	
		
				combinations.append(j[0]+i)

	d7 = combinations # transfer all potential ending six digits to d7 list
	combinations = [] # reset combinations list

	for j in d5: # generate all possible solutions - ending seven digits
		
		for i in d7:
		
			if i[0:2] == j[1:3] and is_Pandigital(int(str(j[0]+i))):	
		
				combinations.append(j[0]+i)
	
	d5 = combinations # transfer all potential ending seven digits to d5 list
	combinations = [] # reset combinations list	
	
	for j in d3: # generate all possible solutions - ending eight digits
		
		for i in d5:
		
			if i[0:2] == j[1:3] and is_Pandigital(int(str(j[0]+i))):	
		
				combinations.append(j[0]+i)	
	
	for i in range(10,100): # add first to numbers to all potential final 8 numbers & general final list
		for j in combinations:
			if is_Pandigital(int(str(i)+j)):
				solution.append(str(i)+j)
	
	combinations = []
	
	for i in list(set(solution)):
		if int(i[1:4]) % 2 == 0:
			combinations.append(int(i))

	print sum(combinations)		
			
	# stop timer and print total elapsed time
	stop = timeit.default_timer()
	print "Total time:", stop - start 		
	
# function for determination of pandigitalness    
def is_Pandigital(n):
	count = 10*[0]
	while n != 0:
		if count[n%10] == 1: return False
		count[n%10] += 1
		n /= 10
	return True		