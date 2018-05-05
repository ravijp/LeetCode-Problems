# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.

# Note:
# 0 ≤ x, y < 231.

# Example:

# Input: x = 1, y = 4

# Output: 2

# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑

# The above arrows point to positions where the corresponding bits are different.

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')
        
###############################################
# python OPERATORS
###############################################
# https://www.programiz.com/python-programming/operators
#

# &	Bitwise AND	x& y = 0 (0000 0000)
# |	Bitwise OR	x | y = 14 (0000 1110)
# ~	Bitwise NOT	~x = -11 (1111 0101)
# ^	Bitwise XOR	x ^ y = 14 (0000 1110)
# >>	Bitwise right shift	x>> 2 = 2 (0000 0010)
# <<	Bitwise left shift	x<< 2 = 40 (0010 1000)
