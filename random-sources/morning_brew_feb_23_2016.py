"""This question was contained in a daily newsletter called Morning Brew. I
decided to use it for my morning code!
A certain street contains 100 buildings. They are numbered from one to
100. How many nines are used in these numbers?"""


def count_vals_in_range(val, low, high):
    """Count the number of times a number appears in a range from low to
    high"""
    # Use list comprehension to create the list of numbers in string form so
    # that they may be joined.
    # Create a string of all numbers in the range from low to high inclusive
    all_nums = "".join([str(num) for num in range(low, (high + 1))])

    # Iterate through the string of numbers and count each time the value occurs
    count = 0
    for char in all_nums:
        if char == str(val):
            count += 1

    return count

# Solving the original question posed:
print count_vals_in_range(9, 1, 100)
