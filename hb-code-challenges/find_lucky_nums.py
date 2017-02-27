"""Return n unique random numbers from 1-10 inclusive.

Given the numbers 1-10, return n random numbers, making sure to never return
the same number twice.  This function will never be called with n < 0 or n > 10.

Ex. >>> lucky_numbers(2) -> [3, 7]

It's legal to ask for no numbers.  >>> lucky_numbers(0) -> []

If we ask for all numbers we shouldn't get any repeats:
>>> sorted(lucky_numbers(10)) -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""

import random


def lucky_numbers(n):
    """Return n unique random numbers from 1-10 inclusive."""
    # Create a list containing the nums to be chosen from
    choices = range(1, 11)
    # Create an empty list to hold the random nums chosen.
    nums = []

    # Return an empty list if 0 nums are requested
    if n == 0:
        return nums
    # Return the list of all choices if 10 nums are requested
    if n == 10:
        return choices

    for i in range(n):
        # Obtain random number and its index
        rand_num = random.choice(choices)
        rand_num_index = choices.index(rand_num)
        # Append random num to nums list and pop from choices list to
        # prevent repeats
        nums.append(rand_num)
        choices.pop(rand_num_index)

    return nums




