"""
This module is a collection of statistical functions for analyzing
the results of a non-nominal survey question.

To test your current solution, run the `test_my_solution.py` file.
Refer to the instructions on Canavs for more information.

Author name: 
I have neither given nor received unauthorized assistance on
this assignment. I did not fabricate the answers to my
survey question.
"""
__version__ = 1

# 0) Question and Results
SURVEY_QUESTION = 'How many pets do you own?'
SURVEY_RESULTS = [1, 2, 2, 1, 1, 2, 2, 1, 1, 1]

# 1) count
def count(list_of_nums: [int])->int:
    '''
    This function takes a list of numbers, calculates the length (# of elements)
    of the list, and returns the length as an integer value.
    
    Args:
        list_of_nums([int]): a list of numbers
    returns:
        int: integer representing length of the list
    '''
    list_length = 0  # initializing list length to 0
    for num in list_of_nums:
        list_length = list_length + 1
    return list_length

# 2) summate
def summate(list_of_nums:[int])->int:
    '''
    This function takes a list of numbers, calculates the sum of all the elements,
    and returns the sum as an integer value.
    
    Args:
        list_of_nums([int]): a list of numbers
    returns:
        int: integer representing the sum of all the elements of the list
    '''
    list_sum = 0 # initializing the list sum to 0
    for num in list_of_nums:
        list_sum = list_sum + num
    return list_sum

# 3) mean
def mean(list_of_nums:[int])->float:
    '''
    This function takes a list of numbers, calculates the mean(average) of all the elements through the mean
    formula, and returns the mean as a float value. If the list is empty, the None value will be returned
    
    Args:
        list_of_nums([int]): a list of numbers
    returns:
        float: float value representing mean value of the list
        None: a special value returne
    '''
    if list_of_nums:
        mean = summate(list_of_nums)/count(list_of_nums) # calling the summate and count functions for simplification.
        mean = round(mean, 2) # using the round function to round to 2 decimal places
    else:
        mean = None
    return mean

# 4) maximum
def maximum(list_of_nums:[int])->int:
    '''
    This function takes a list of numbers, and returns the maximum(largest) value
    of the list as an integer value. If the list is empty, the None value will be returned.
    
    Args:
        list_of_nums([int]): a list of numbers
    returns:
        int: integer representing the maximum value of the list
        None: a special value returne
    '''
    max_num = -1000 # initializing the max number variable to an arbitrary number smaller than any of the list elements
    for num in list_of_nums:
        if num > max_num:
            max_num = num
    if not list_of_nums:
        max_num = None
    return max_num

# 5) minimum
def minimum(list_of_nums:[int])->int:
    '''
    This function takes a list of numbers, and returns the minimum(smallest) value
    of the list as an integer value. If the list is empty, the None value will be returned.
    
    Args:
        list_of_nums([int]): a list of numbers
    returns:
        int: integer representing the minimum value of the list
        None: special value returned when empty list is inputted
    '''
    min_num = 1000 # initializing the min number variable to an arbitrary number larger than any of the list elements
    for num in list_of_nums:
        if num < min_num:
            min_num = num
    if not list_of_nums:
        min_num = None
    return min_num

# 6) median
def median(list_of_nums:[int])->float:
    '''
    This function takes a list of numbers, and calculates the median value by
    indexing the list by its middle index. The median is then returned as a float value.
    If the list is empty, the None value will be returned.
    
    Args:
        list_of_nums([int]): a list of numbers
    returns:
        float: float representing median value of the list
        None: special value returned when empty list is inputted
    '''
    list_of_nums = sorted(list_of_nums) # using the sorted function to sort the list in ascending order
    if list_of_nums:
        middle_index = int((count(list_of_nums)/2)) # Formula for calculating middle index of a list.
        # we convert the value to int, since indexing only allows int values.
        median = list_of_nums[middle_index] # indexing the list with the computed middle index
    else:
        median = None
    return median

# 7) square
def square(list_of_nums:[int])->list:
    '''
    This function takes a list of numbers, and returns a new list in which each element
    of the inputted list has been squared.
    
    Args:
        list_of_nums([int]): a list of numbers
    returns:
        list: a new list that is returned, featuring the squares of all of the elements of the
        inputted list
    '''
    list_squared = []
    for num in list_of_nums:
        list_squared.append(num**2) # Appending the square of all the elements of the inputted list
    return list_squared

# 8) standard_deviation
def standard_deviation(list_of_nums:[int])->float:
    '''
    This function takes a list of numbers, and returns the standard deviation
    of all the elements as a float value. If the list is empty, the None value will be returned.
    
    Args:
        list_of_nums([int]): a list of numbers
    returns:
        float: float value is returned, representing the standard deviation of the list
        None: special value returned when empty list is inputted
    '''
    if count(list_of_nums) >= 2:
        standard_dev = (((summate(square(list_of_nums)))-(summate(list_of_nums)**2)/
                       (count(list_of_nums)))/(count(list_of_nums)-1))**.5
        # This is the formula for calculating the standard deviation
    else:
        standard_dev = None
    return standard_dev

# The following code can be used to try out your functions.
# Uncomment each line as you implement the functions to try them out.
# When you have implemented each function, copy the output from the
#   console into a comment below.
    
print("We asked", count(SURVEY_RESULTS), "people the following question.")
print('"How many pets do you own?"')
print("Here are the statistical results:")
print("\tSum:", summate(SURVEY_RESULTS))
print("\tMean:", mean(SURVEY_RESULTS))
print("\tMedian:", median(SURVEY_RESULTS))
print("\tMaximum:", maximum(SURVEY_RESULTS))
print("\tMinimum:", minimum(SURVEY_RESULTS))
print("\tSquare:", square(SURVEY_RESULTS))
print("\tStandard Deviation:", standard_deviation(SURVEY_RESULTS))
# Final Survey Statistics:
# Sum: 14
# Mean: 1.4
# Median: 1
# Maximum: 2
# Minimum: 1
# Square: [1, 4, 4, 1, 1, 4, 4, 1, 1, 1]
# Standard Deviation: 0.5163977794943221

# How these results will help us crush these puny humans:
# It seems that these humans are deeply infatuated with what they call their "Pets",
# With this rather obsessive behavior surrounding these creatures known as "Puppies" and "Kittens".
# With this, we have the chance to invade their planet while they're distracted. Furthermore, we can use our own
# other wordly appearance to behave as "Pets" in front of these mere humans, lowering their guard, increasing
# our chances to thrive in their resource-rich world.
