## Problem 33

## The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly 
## believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

## We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

## There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

## If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

# define function
def fract():
    
    # import timeit and start timer to measure time of function
    import timeit
    start = timeit.default_timer()
    
    solution = [] # initialize solution list for holding all initially screened potential #s
    answer = [] # initialize answer list for holding all final fractions given characteristics noted in problem
    numerator = 1 # initialize numerator for final solution generation
    denominator = 1 # initialize denominator for final solution generation
    
    for i in range(10,100): # iterate through all possible numerators
    
        for j in range(10,100): # iterate through all possible denominators
        
            if i < j: # only check fractions if they are less than 1 per question
        
                if i%10 != 0 and j%10 !=0: # modular function removes trivial examples of 10s digits per question
        
                    if (float(i) / float(j)) == (float(str(i)[0]) / float(str(j)[0])) or (float(i) / float(j)) == (float(str(i)[1]) / float(str(j)[1])) or (float(i) / float(j)) == (float(str(i)[0]) / float(str(j)[1])) or (float(i) / float(j)) == (float(str(i)[1]) / float(str(j)[0])): 
                    # generates screen of potential fractions where fraction solution equals fraction solution when one digit from both numerator and denominator 
                    # are removed - step wasn't necessary but was retained as that's how code development played out
                    
                        solution.append((i,j)) # first screen of potential fractions appended per above screen
    
    for k in range(0,10): # checks digits 0-9 in fractions for potential removal
    
        for l in range(0,(len(solution) - 1)): # checks each tuple in solution list for conditions matching question
         
            # wrote four potential variations for fulfilling question conditions below depending on digits place in numerator and denominator
         
            if str(k) == str(solution[l][0])[0] and str(k) == str(solution[l][1])[0]: # checks if digit is the same in numerator and denominator spot
                
                if float(solution[l][0]) / float(solution[l][1]) == float(str(solution[l][0])[1]) / float(str(solution[l][1])[1]): # checks if fraction equals "reduced" fraction once common number from either digit in both numerator and denominator is removed
                
                    answer.append(solution[l]) # appends fraction to answer list
                                
            if str(k) == str(solution[l][0])[0]and str(k) == str(solution[l][1])[1]:
            
                if float(solution[l][0]) / float(solution[l][1]) == float(str(solution[l][0])[1]) / float(str(solution[l][1])[0]):
                
                    answer.append(solution[l])
            
            if str(k) == str(solution[l][0])[1]and str(k) == str(solution[l][1])[0]:    
            
                if float(solution[l][0]) / float(solution[l][1]) == float(str(solution[l][0])[0]) / float(str(solution[l][1])[1]):
                
                    answer.append(solution[l])
            
            if str(k) == str(solution[l][0])[1]and str(k) == str(solution[l][1])[1]:
            
                if float(solution[l][0]) / float(solution[l][1]) == float(str(solution[l][0])[0]) / float(str(solution[l][1])[0]):
                
                    answer.append(solution[l])            
                           
    for m in range(0,(len(answer))): # iterates through fractions in answer list and finds product of all numerators and denominators and reduces fraction and returns reduced denominator product solution as per question
    
        numerator = numerator * answer[m][0]
        
        denominator = denominator * answer[m][1]
     
        print answer[m][0], answer[m][1]
    
    print denominator / numerator # prints solution
   
    # stop timer and print total elapsed time
    stop = timeit.default_timer()
    print "Total time:", stop - start, "seconds"