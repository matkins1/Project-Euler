## Problem 42

## The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); 
## so the first ten triangle numbers are:

## 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

## By converting each letter in a word to a number corresponding to its alphabetical position 
## and adding these values we form a word value. For example, the word value for 
## SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call 
## the word a triangle word.

## Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing 
## nearly two-thousand common English words, how many are triangle words?

# function to search for coded triangle numbers in words.txt
def tri_Numbers():

	import timeit # import timeit and start timer to measure time of function
	start = timeit.default_timer()
	
	import urllib2 # import urllib2 package to download words.txt file from Project Euler website
	
	data = urllib2.urlopen("https://projecteuler.net/project/resources/p042_words.txt") # download words.txt and store in "data" object
	
	word_data = [] # initialize word_data list to store words.txt data 
	word_list = [] # initialize word list for data transformation
	
	dict = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26} 
	#initialize dictionary for conversion of letters to numbers
	
    # transform words.txt "data" object to "word_data" list
	for line in data:
		
		word_data.append(line)
	
	word_list = word_data[0].split(',') # separate words into list elements
    
	word_data = [] # reset word_data 
	
	for i in word_list:
        word_data.append(i.replace('"',''))
	
	word_list = [] # reset word_list
	
	for i in word_data: # iterate through words in words.txt file and return numeric values based on letter values in "dict"
		count = 0
		for j in i:
			count += dict[j]
		
		word_list.append(count) # append all word values to word_list for checking whether they are triangular
	
	word_list = sorted(word_list, reverse=True) # sort word_list in descending order to determine largest triangle number that needs generating
	
	n = 0 # initialize integer to iterate to create triangle numbers
	
	triangle_numbers = [] # initialize list to hold all triangle numbers
	
	while .5*n*(n+1) < word_list[0]: # create triangle numbers up to largest integer in word_list
		
		n += 1 # iterate n to create additional triangle number
		
		triangle_numbers.append(int(.5*n*(n+1))) # generate triangle number and append to triangle_numbers list
	
	solution = 0 # initialize solution variable to count number of triangle numbers in word_list
	
	for i in word_list: # check if each number in word_list is a triangle number and iterate count of total triangle numbers
	
		if i in triangle_numbers:
		
			solution += 1
	
	print solution # print count of triangle numbers in word_list
	
    # stop timer and print total elapsed time
    stop = timeit.default_timer()
    print "Total time:", stop - start 