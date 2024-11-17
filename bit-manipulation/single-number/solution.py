"""
Given a non-empy array of integers nums, every element appears twice except for one.
Find that single one.

The solution must have a linear runtime complexity, and use constant extra space.

Example:
nums = [4, 1, 2, 1, 2]
returns: 4

Solution:
- use XOR
    - any number XOR itself will give us 0
    - any number XOR 0 is just the number
- since there are 2 of every number, but one, we just XOR everything and return the final value (which should be itself)

Complexity
- Time: O(n)
- Space: O(1)
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0

        for x in nums:
            # XOR in python
            a ^= x

        return a
