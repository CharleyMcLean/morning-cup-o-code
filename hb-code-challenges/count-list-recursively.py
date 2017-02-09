"""Count the number of items in a list, using recursion.
For example, given [], return 0; given [1, 2, 3], return 3."""


def count_recursively(lst):
    """Return number of items in a list, using recursion.
        >>> count_recursively([])
        0
        >>> count_recursively([1, 2, 3])
        3
    """
    if not lst:
        return 0

    # without recursion:
    # counter = 0
    # for item in lst:
    #     counter += 1
    # return counter

    # recursively:
    return 1 + count_recursively(lst[1:])


##########################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()

    print
    if not result.failed:
        print "All tests passed!"
    print
