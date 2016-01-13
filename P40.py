## Problem 40

## An irrational decimal fraction is created by concatenating the positive integers:

## 0.123456789101112131415161718192021...

## It can be seen that the 12th digit of the fractional part is 1.

## If d^n represents the nth digit of the fractional part, find the value of the following expression.

## d^1 × d^10 × d^100 × d^1000 × d^10000 × d^100000 × d^1000000


def chap():

	# import timeit and start timer to measure time of function
	import timeit
	start = timeit.default_timer()	

	n = 0 # initialize integer to add iterations to Champernowne's constant
	n_length = 0 # initialize value to hold length of Champernowne's constant to compare to D
	d = 1 # initialize d value to iterate by ten per question
	digit_list = [] # initialize solution list to hold each of 7 digits per question
	solution = 1 # initialize solution to multiply each of 7 digits from digits_list
	
	while n_length < 1000000: # find each of 7 digits per question by iterating through digits
	
		n += 1
		n_length += len(str(n))
		
		if n_length >= d:
		
			digit_list.append(int(str(n)[-1*(n_length - d)-1]))
			
			d *= 10

	for i in digit_list: # multiply all digits in digits_list together
	
			solution = solution * i
			
	print solution		
	
	# stop timer and print total elapsed time
	stop = timeit.default_timer()
	print "Total time:", stop - start, "seconds"	