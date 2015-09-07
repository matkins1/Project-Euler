## Problem 35

## The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

## There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

## How many circular primes are there below one million?

def circ_prime():
    
    # import timeit and start timer to measure time of function
    import timeit
    start = timeit.default_timer()
       
    list2 = prime_list(1000000) # import list of potential prime number candidates for solution - calls "prime_list" formula
    temp_list = [] # initialize temp_list to hold all digits in circular prime candidate list2 above
    rotate_list = [] # initialize rotate_list to hold all rotations of each circular prime candidate from above temp_list
    final_list = [2,5,3,7] # initialize final_list to hold all circular primes
    all_prime = 0 # initialize all_prime variable to iterate for all prime rotations 
    k_test = 0 # initialize variable to hold integer concatenation of tuples in rotate_list below
    
    for i in list2: # iterates through each circular prime candidate
    
        temp_list = [] # reset temp_list
        rotate_list = [] # reset rotate_list
        all_prime = 0 # reset all_prime
        k_test = 0 # reset k_test
    
        for j in str(i): # iterates through each digit in circular prime candidates
        
            temp_list.append(int(j)) # holds digits for each circular prime candidate checked

        rotate_list = Rotations(temp_list) # rotate each circular prime candidate - calls "Rotations" formula  
        
        for k in rotate_list: # iterates through each rotation in rotate_list
    
            k_test = int(''.join(map(str,k))) # concatenate each tuple tested to an integer from individual digits
    
            if is_Prime(k_test): # check primality of each rotation - calls "is_Prime" formula 
                
                all_prime += 1 # iterate variable if prime
        
            if all_prime == len(rotate_list): # if each rotation is prime...
                
                final_list.append(i) # append number in list2 to final_list
        
    print len(final_list) # return solution
    print final_list # return all circular primes
    
    # stop timer and print total elapsed time
    stop = timeit.default_timer()
    print "Total time:", stop - start, "seconds"

# function to generate list of primes less than n (also has embedded code to exclude all #s containing "0,2,4,6,8" for quicker processing pertaining to this specific problem
def prime_list(n):    
    
    list3 = [] # 2, 3, 5, 7 are added directly to "final_list" in above code as they are skipped in below range due to difficulties in "circ_prime" code
    
    for i in range(8,n): # iterates through all numbers in range
        
        if "0" not in str(i) and "2" not in str(i) and "4" not in str(i) and "5" not in str(i) and "6" not in str(i) and "8" not in str(i): # add'l code to remove all #s with 0,2,4,6,8 as these cannot be "circular primes"
        
            if is_Prime(i): # checks if number in range is prime
        
                list3.append(i) # appends number to list if prime
            
    return list3 # returns list of prime numbers (excluding 2,3,5, & 7 which are re-added in circ_prime code above)
    
# function for determination of primality    
def is_Prime(n):
    if n < 2: # returns false if number is less than 2
        return False
    if n == 2: # returns true if number is 2
       return True
    if n % 2 == 0: # returns true if number is even
        return False
    
    i = 3 # iterates through all possible divisors of number up to the square root of that number and returns true if not divisible by any number
    
    while i <= n**.5:
        if n % i == 0:
            return False
        i = i+2
    return True 

# function to rotate each circular prime candidate    
def Rotations(n):
    Rotations = []
    x = 0
    while x < len(n):
        n.insert(0,n.pop())
        Rotations.append(list(n))
        x += 1
    return Rotations