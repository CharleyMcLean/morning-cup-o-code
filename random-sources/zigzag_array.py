"""Given an array of positive and negative integers, representing distances
north and south, we want to see the elements of the array in zigzag order.
This means the largest number appears first, the smallest appears second, and
the remaining elements alternate between the larger memebers decreasing from
the largest, and the smaller members increasing from the smallest.

Ex. [1, 3, 6, 9, -3] --> [9, -3, 6, 1, 3]

Input - an integer array of n integers
Contraints: 2 <= n <= 10^4, elements of the array may include duplicates
Output - the array in zigzag order

ex. [7, 5, 2, 7, 8, -2, 25, 25] --> [25, -2, 25, 2, 8, 5, 7]
"""

def  wiggleArrangeArray( intArr):
    #Sort the array in reverse so that largest value is first
    intArr.sort(reverse=True)
    #Create a pointer for the index of the current highest and lowest values (left and right)
    left = 0
    right = -1
    
    zigzag = []
    for i in range(len(intArr) / 2):
        zigzag.append(intArr[left])
        zigzag.append(intArr[right])
        left += 1
        right -= 1
    
    #Must account for when an integer doesn't get swapped
    if len(intArr) % 2 != 0:
        zigzag.append(intArr[len(intArr) / 2])

    return zigzag