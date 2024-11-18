"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:
nums = [1, 2, 3, 1]
returns: True

Example 2:
nums = [1, 2, 3, 4]
returns False

Solution:
- use a hash set (set) to add each umber of nums to
- before adding an number to the set, see if nums is already in it
- if nums is in it, return True, if all elements are seen and no elements have been seen before, return False

Complexity
- Time: O(n)
- Space: O(n)
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()

        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False
