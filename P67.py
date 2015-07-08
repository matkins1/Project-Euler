## Problem 67

## By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

## 3
## 7 4
## 2 4 6
## 8 5 9 3

## That is, 3 + 7 + 4 + 9 = 23.

## Find the maximum total from top to bottom in triangle.txt [https://projecteuler.net/project/resources/p067_triangle.txt] (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

## NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
## it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

# define function
def max_path_sum2():
    
    # import timeit and start timer to measure time of function
    import timeit
    start = timeit.default_timer()
    
    # import urllib2 package to download triangle.txt file from Project Euler website
    import urllib2 
    
    # download triangle.txt and store in "data" object
    data = urllib2.urlopen("https://projecteuler.net/project/resources/p067_triangle.txt") 
    
    # initialize tri_data list to store triangle.txt data and triangle list for data transformation
    tri_data = [] 
    triangle = []
    
    # transform triangle.txt "data" object to "triangle" matrix
    for line in data:
        tri_data.append(line)
    
    # splits each item in list
    for h in tri_data:
        triangle.append(h.split(" ")) 
    
	# iterate over rows of triangle
    for i in range(1, len(triangle)): 
		
		# iterate over items of reach row of triangle
        for j in range(0, len(triangle[i-1])):    
			
			# replace each element of "triangle" below first row with the max sum of element and above adjacent elements
            triangle[i][j] = max(int(triangle[i-1][j-1]),int(triangle[i-1][j])) + int(triangle[i][j])
					
		# appends sum for final element in row i of triangle - had to add this outside "j" iteration due to out of range list index
        triangle[i][len(triangle[i-1])] = int(triangle[i-1][len(triangle[i-1])-1]) + int(triangle[i][len(triangle[i-1])])	    
	
    # returns maximum sum in final row of "triangle" matrix
    print max(triangle[len(triangle)-1])    
    
    # stop timer and print total elapsed time
    stop = timeit.default_timer()
    print "Total time:", stop - start 