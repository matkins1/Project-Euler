## Problem 19

## You are given the following information, but you may prefer to do some research for yourself.

##    1 Jan 1900 was a Monday.
##    Thirty days has September,
##    April, June and November.
##    All the rest have thirty-one,
##    Saving February alone,
##    Which has twenty-eight, rain or shine.
##    And on leap years, twenty-nine.
##    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

## How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

## Code below

# define function
def count_sunday():
    
    # import timeit and start timer to measure time of function
    import timeit
    
    start = timeit.default_timer()
    import itertools # import itertool package for iterating over weekday names
    
    list = [] # initialize list to hold all values
    month = 1 # set month = January
    day_name = ["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday"] # initialize day name list
    weekday = itertools.cycle(day_name)
	
    for j in range(1901,2001): # perform iterations from 1901 through 2000
		
        month = 1 # resets month after iteration below
		
        for i in range(1,32): # iterates through days in january
            list.append([i,next(weekday)]) # append combination to list - uses itertools package to iterate through weekdays
			## note the list.append code above includes only weekday and day of month since that's what answer looks for. could have added in "j" for year and "month" for month to get complete date
			
        month += 1 # iterates month		
		
        if (j % 4) == 0: # checks leap year condition - no check on century divisible by 400 as script iterates through single century
		
            for i in range(1,30):
                list.append([i,next(weekday)]) # append combination to list - uses itertools package to iterate through weekdays
			
            month += 1 # iterates month	
		
        else: # checks leap year condition - no check on century divisible by 400 as script iterates through single century
		
            for i in range(1,29):
                list.append([i,next(weekday)]) # append combination to list - uses itertools package to iterate through weekdays
			
            month += 1 # iterates month	
		
        for i in range(1,32): # iterates through days in march
            list.append([i,next(weekday)]) # append combination to list - uses itertools package to iterate through weekdays
			
        month += 1 # iterates month			
	
        for i in range(1,31): # iterates through days in april
            list.append([i,next(weekday)]) # append combination to list - uses itertools package to iterate through weekdays
			
        month += 1 # iterates month			

        for i in range(1,32): # iterates through days in may
            list.append([i,next(weekday)]) # append combination to list - uses itertools package to iterate through weekdays
			
        month += 1 # iterates month		

        for i in range(1,31): # iterates through days in june
            list.append([i,next(weekday)]) # append combination to list - uses itertools package to iterate through weekdays
			
        month += 1 # iterates month		
		
        for i in range(1,32): # iterates through days in july
            list.append([i,next(weekday)]) # append combination to list - uses itertools package to iterate through weekdays
			
        month += 1 # iterates month			
		
        for i in range(1,32): # iterates through days in august
            list.append([i,next(weekday)]) # append combination to list - uses itertools package to iterate through weekdays
			
        month += 1 # iterates month		
		
        for i in range(1,31): # iterates through days in september
            list.append([i,next(weekday)]) # append combination to list - uses itertools package to iterate through weekdays
			
        month += 1 # iterates month			
		
        for i in range(1,32): # iterates through days in october
            list.append([i,next(weekday)]) # append combination to list - uses itertools package to iterate through weekdays
			
        month += 1 # iterates month			
		
        for i in range(1,31): # iterates through days in november
            list.append([i,next(weekday)]) # append combination to list - uses itertools package to iterate through weekdays
			
        month += 1 # iterates month		
		
        for i in range(1,32): # iterates through days in december
            list.append([i,next(weekday)]) # append combination to list - uses itertools package to iterate through weekdays
	
    answer = [item for item in list if 1 in item] # output all first days of month in "list" to "answer" 
	
    answer = [item for item in answer if "Sunday" in item] # refine "answer" for all sundays
	
    print len(answer) # return number of sundays on first day of month for period
	
    # stop timer and print total elapsed time
    stop = timeit.default_timer()
    print "Total time:", stop - start 