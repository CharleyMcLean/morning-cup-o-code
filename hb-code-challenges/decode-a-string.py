"""In this challenge, you'll write a decoder.  A valid code is a sequence of
numbers and letters, always starting with a number and ending with letter(s).
Each  number tells you how many characters to skip before finding a good letter.
After each good letter should come the next number.  For example, the string
"hey" could be encoded by "0h1ae2bcy".  This means "skip 0, find the 'h',
skip 1, find the 'e', skip 2, find the 'y'."""


def decode(s):
    """Write a function to decode the input string based on the challenge
    description.
        >>> decode("0h")
        'h'
        >>> decode("0h1ae2bcy")
        'hey'
    """

    decoded = []
    index = 0
    while index < len(s):
        num_to_skip = int(s[index])
        index += num_to_skip + 1
        decoded.append(s[index])
        index += 1

    return "".join(decoded)


#########################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()

    print
    if not result.failed:
        print "ALL TESTS PASSED"
    print
