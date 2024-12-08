"""
Given an array fo integers 'nums' which is sorted in ascending order, and an integer 'target', write a function to search
'target' in 'nums'. If 'target' exists, then return its index. otherwise, return -1.

Example:
nums = [-1, 0, 3, 5, 9, 12]
target = 9
returns: 4

Solution:
- Binary search
- use left and right to mark our search space
- if target is greater than middle, update left to middle
- if target is less tha middle, update right midle
- if target is equal to middle, return middle

Complexity:
- Time: O(log n)
- Space: O(1)
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1

        return -1
