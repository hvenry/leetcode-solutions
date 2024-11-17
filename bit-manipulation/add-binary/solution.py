"""
Given two binary strings a and b, return their sum as a binary string.

Example:
Input: a = "11", b = "1"
Output: "100"

11=3 + 1=1 is equal to 100, 4.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # init an empy list to store result as characters
        res = []
        # init a carry value to handle binary addition carryovers
        carry = 0

        # Pointers to the last characters (lest significatn bits of a and b)
        i, j = len(a) - 1, len(b) - 1

        # loop as long as there are bits eft in a or b, or there is a carry.
        while i >= 0 or j >= 0 or carry:
            # get the current bit of a and b (from the end). if out of bounds, assuem 0
            d1 = int(a[i]) if i >= 0 else 0
            d2 = int(b[j]) if j >= 0 else 0

            # calculate the sum of bits and the carry
            s = d1 + d2 + carry
            # update the carry, 1 if sum >= 2, otherwise 0
            carry = s // 2
            # Calculate the current bit for the result (0 or 1)
            rem = s % 2
            res.append(str(rem))

            # move to the next bits in a and b (leftwards)
            i -= 1
            j -= 1

        # join the reversed list as a single string
        return "".join(res[::-1])
