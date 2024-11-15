"""
Given an ingteger array nums sorted in non-decreasing order, remove the duplicates in-place such that each
unique element appears only once. The relative order of the elements should be kept the same. Then return
the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following steps:

- Change the array nums such that the first k elements of nums contain the unique elements in the order they were
  present in nums initially.
- Return k

Example 1:
input: nums = [1, 1, 2]
output: nums = [1, 2, _]
returns: 2

Example 2:
input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
output: nums = [0, 1, 2, 3, 4]
returns: 4

Solution O(n):
- use two pointers, i and j, both starting at the first index
- compare i - 1 and i, and we keep moving until we don't find a duplicate (number i-1 is different from i)
- when we find a unique value, we send it to j's position, then we move j over, all the numbers behind j are unique
- when i reaches the end, the number of unique values is the index of j

Complexity:
    Time: O(n)
    Space: O(1)
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        j = 1

        for i in range(1, n):
            # no duplicate
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1

        return j
