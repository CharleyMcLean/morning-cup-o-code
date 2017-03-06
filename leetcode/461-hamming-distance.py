"""The Hamming distance between two integers is the number of positions at
which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note 0 <= x, y <= 2^31.

Example:
Input:  x = 1, y = 4
Output:  2

Explanation:
1 (0 0 0 1)
4 (0 1 0 0)
     ^   ^
The above arrows point to positions where the corresponding bits are different.
"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # First we need to convert both x and y to binary.  For now, we'll
        # create a list for both to hold their bits.  We know that both x and y
        # are less than 2^31, so we'll start there.  It's not the most
        # economical option, but we can refactor after we get a working solution.
        x_bits = []
        y_bits = []

        x_bits = convert_to_bits(x, x_bits)
        y_bits = convert_to_bits(y, y_bits)

        # Now we must see which bits differ.
        count = 0
        for i in range(len(x_bits)):
            if x_bits[i] != y_bits[i]:
                count += 1

        return count


def convert_to_bits(num, lst):
    power = 31
    while power >= 0:
        if num >= 2 ** power:
            lst.append(1)
            num -= 2 ** power
        else:
            lst.append(0)
        power -= 1

    return lst


############################################################################
test = Solution()
print "Expecting 2, got: " + str(test.hammingDistance(1, 4))