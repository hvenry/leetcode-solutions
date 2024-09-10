from typing import List

"""
write a function that reverses a string, the input string is given as an array of characters s.

Modify the array  in place with O(1) extra memory.

Input: s = ["h", "e", "l", "l", "o"]
Output: ["o", "l", "l", "e", "h"]

solution: use two pointers.
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        left = 0  # end

        # hello -> len = 5, so we want -1 to get end index
        right = len(s) - 1

        # iterate until left is no longer less than right, meaning our pointers have intersected
        while left < right:
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1
