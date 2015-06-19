## Problem 17

## If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

## If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

## NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

# define function
def letter_sum():
    
    # import timeit and start timer to measure time of function
    import timeit
    start = timeit.default_timer()
    
    # declare variables for letters in each component of integer
    # variables of hundred values include the word "and" in their letter count
    # "a00" variable used to remove the "and" from even multiples of 100
    # will need to add "11" to final total since 1,000 isn't evaluated here
    a0 = 0; a00 = -3; a1 = 3; a2 = 3; a3 = 5; a4 = 4; a5 = 4; 
    a6 = 3; a7 = 5; a8 = 5; a9 = 4; a01 = 3; a02 = 3; a03 = 5; 
    a04 = 4; a05 = 4; a06 = 3; a07 = 5; a08 = 5; a09 = 4; a10 = 3; 
    a11 = 6; a12 = 6; a13 = 8; a14 = 8; a15 = 7; a16 = 7; a17 = 9; 
    a18 = 8; a19 = 8; a20 = 6; a30 = 6; a40 = 5; a50 = 5; a60 = 5; 
    a70 = 7; a80 = 6; a90 = 6; a100 = 13; a200 = 13; a300 = 15; 
    a400 = 14; a500 = 14; a600 = 13; a700 = 15; a800 = 15; a900 = 14 

    #declare list for holding sum of values
    sum_list = []

    # iterate from 1 to 999 (sum of 1,000 to be added at end) 
    for i in range(1,1000):
    
        # declare "list" variable for use of decomposing integers
        list = []

        # integer to string class and store in "my_int"
        my_int = str(i)
    
     # code for value less than 20
        if i < 20:
            sum_list.append("a" + str(i)) # store values for tens/singles place
    
     # code for value from 20 through 99    
        elif i > 19 and i < 100:
        
            # iterate through integer and store individual digits in "list"
            for j in my_int:
                list.append(int(j))
        
            sum_list.append("a" + str(i)[0] + "0") # store values for tens digit place
            sum_list.append("a" + str(i)[1]) # store values for ones digit place
    
        # code for value from 100 through 999 
        else:
            # iterate through integer and store individual digits in "list"
            for j in my_int:
                list.append(int(j))
            
            # if number is even hundred store values in "00" case manner
            if int(str(list[1]) + str(list[2])) == 0:
                sum_list.append("a" + str(i)[0] + "00") # store values for hundreds digit place
                sum_list.append("a00") # store "0" value
        
            # code for value from x01 through x19
            elif int(str(list[1]) + str(list[2])) < 20:
                sum_list.append("a" + str(i)[0] + "00") # store values for hundreds digit place
                sum_list.append("a" + str(list[1]) + str(list[2])) # store values for tens/singles place  
              
            # code for value from x20 onward
            else:
                sum_list.append("a" + str(i)[0] + "00") # store values for hundreds digit place
                sum_list.append("a" + str(list[1]) + "0") # store values for tens place
                sum_list.append("a" + str(list[2])) # store values for singles place 
    
    # initialize variable to hold final sum value and add "11" for 1,000
    final_sum = [11]
    
    # iterate over sum list and return values for each stored variale and append to "final_sum"
    for k in sum_list:
        final_sum.append(eval(k))      
    
    # print solution
    print sum(final_sum)
    
    # stop timer and print total elapsed time
    stop = timeit.default_timer()
    print "Total time:", stop - start 