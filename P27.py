## Problem 27

## Euler discovered the remarkable quadratic formula:

## n**2 + n + 41

## It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. 
## However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

## The incredible formula  n**2 − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. 
## The product of the coefficients, −79 and 1601, is −126479.

## Considering quadratics of the form:

##    n**2 + an + b, where |a| < 1000 and |b| < 1000

##    where |n| is the modulus/absolute value of n
##    e.g. |11| = 11 and |−4| = 4

## Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes 
## for consecutive values of n, starting with n = 0.

# code for determination of number primality
def is_Prime(n):
    if n < 2: # returns false if number is less than 2
        return False
    if n == 2: # returns true if number is 2
       return True
    if n % 2 == 0: # returns true if number is even
        return False
    
    # iterates through all possible divisors of number up to the square root of that number and returns true if not divisible by any number
    i = 3
    
    while i <= n**.5:
        if n % i == 0:
            return False
        i = i+2
    return True 
 
# define function
def quad_primes():

    # import timeit and start timer to measure time of function
    import timeit
    start = timeit.default_timer()
    
    # initialize list of all b values - all are prime numbers as b must be prime since n**2 + an + b where n and a = 0 must be prime
    b_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 
    127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 
    269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 
    431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 
    599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 
    761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 
    947, 953, 967, 971, 977, 983, 991, 997, -2, -3, -5, -7, -11, -13, -17, -19, -23, -29, -31, -37, -41, -43, -47, -53, -59, -61, -67, 
    -71, -73, -79, -83, -89, -97, -101, -103, -107, -109, -113, -127, -131, -137, -139, -149, -151, -157, -163, -167, -173, -179, -181, 
    -191, -193, -197, -199, -211, -223, -227, -229, -233, -239, -241, -251, -257, -263, -269, -271, -277, -281, -283, -293, -307, -311, 
    -313, -317, -331, -337, -347, -349, -353, -359, -367, -373, -379, -383, -389, -397, -401, -409, -419, -421, -431, -433, -439, -443, 
    -449, -457, -461, -463, -467, -479, -487, -491, -499, -503, -509, -521, -523, -541, -547, -557, -563, -569, -571, -577, -587, -593, 
    -599, -601, -607, -613, -617, -619, -631, -641, -643, -647, -653, -659, -661, -673, -677, -683, -691, -701, -709, -719, -727, -733, 
    -739, -743, -751, -757, -761, -769, -773, -787, -797, -809, -811, -821, -823, -827, -829, -839, -853, -857, -859, -863, -877, -881, 
    -883, -887, -907, -911, -919, -929, -937, -941, -947, -953, -967, -971, -977, -983, -991, -997]
      
    solution = [] # initialize solution list
        
    for b in b_list: # iterates through b values in b_list - all prime numbers
        
        n = 0
        list = []
        
        for a in range(-999,1000): # iterates through all a values per problem question
            
            if b > -(40**2 + 40*a): # quick check given hint in solution for Euler's quadratic prime formula "n**2 + n + 41"
                
                n = 0
                list = []                      
                
                while is_Prime(n**2 + a*n + b): # checks if formula produces a prime number
        
                    list.append(n**2 + a*n + b) # if the formula produces a prime #, append to list
        
                    n += 1
                
                solution.append((len(list),a,b)) # append (# of primes produced, a value, b value) for all combinations          
                   
    print sorted(solution, reverse=True)[0][1] * sorted(solution, reverse=True)[0][2] # prints the product of the a and b values that produces the largest number of primes
    
    # stop timer and print total elapsed time
    stop = timeit.default_timer()
    print "Total time:", stop - start, "seconds" 