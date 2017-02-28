"""Consider an array of n integers where all but one of the integers occurs
in pairs.  In other words, each element occurs exactly twice except for one
element.

Complete the lonelyInteger function - it has one parameter, an array of
integers.  The function must find and return an integer denoting the unique
element in the array.

Constraints: 1 <= n <= 100, n is odd

Output: Function must return an integer denoting the unique element in the
array.

Example:
[1] --> 1
[1, 1, 2] --> 2
"""

def  lonelyInteger( arr):
    #Create a dictionary to hold counts
    counts = {}
    for num in arr:
        counts[num] = counts.get(num, 0) + 1
    
    #Use list comprehension to find key with value of 1
    unique = [key for key, value in counts.iteritems() if value == 1]

    # Unique integer is stored in a list
    return unique[0]