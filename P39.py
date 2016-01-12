## Problem 39

## If p is the perimeter of a right angle triangle with integral length sides, 
## {a,b,c}, there are exactly three solutions for p = 120.

## {20,48,52}, {24,45,51}, {30,40,50}

## For which value of p ≤ 1000, is the number of solutions maximised?

# function to find integer right triangle maximized solution
def rt():
		
	# import timeit and start timer to measure time of function
	import timeit
	start = timeit.default_timer()	

	list = [] # initalize list to hold tuples
	list2 = [] # initialize new list to hold distinct values of list
	solution = [] # initalize solution
	a, b, c = 0, 0, 0 # initialize a, b, c
	
	while a <= 500: # lazy way to code iterating through all possible combos < p = 1000 for pythagorean triplets
			
		b = 0
			
		while b <= 500:
		
			c = 0
		
			while c <= 500:				
				
				if a*a + b*b == c*c:
				
					if c > b > a:
					
						list.append((a,b,c,a+b+c))
						
					if c > a > b:
					
						list.append((b,a,c,a+b+c))	
					
					if b > c > a:
					
						list.append((a,c,b,a+b+c))	

					if b > a > c:
					
						list.append((c,a,b,a+b+c))
						
					if a > c > b:
					
						list.append((b,c,a,a+b+c))	
						
					if a > b > c:
					
						list.append((c,b,a,a+b+c))		
						
				c += 1
				
			b += 1
			
		a += 1
	
	for i in list: # append unique values to list2
		if i not in list2 and i[3] <=1000:
			list2.append(i)
	
	for j in list2: # add p-values to solution for searching most frequent below
	
		solution.append(j[3])
	
	solution.sort(reverse=True) # sort solution
	
	return max(set(solution), key=solution.count) # return most frequent p-value
		
	# stop timer and print total elapsed time
	stop = timeit.default_timer()
	print "Total time:", stop - start, "seconds"