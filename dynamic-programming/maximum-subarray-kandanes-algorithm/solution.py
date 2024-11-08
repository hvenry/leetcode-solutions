"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
output: 6

The subarray [4, -1, 2, 1] has the largest sum of 6.


Example 2:
nums = [-2, 7, -3, 4]
output = 8 -> [7, -3, 4]

How do we get this?

index 0: -2
cur_sum = -2 -> negative cur_sums are discarded and set back to 0 (start window again)
max_sum = -2

index 1: 7
cur_sum: 7
max_sum = 7

index 2: -3
cur_sum: 4
max_sum: 7

index 3: 4
cur_sum: 8
max_sum: 8

Solution:
Bottom up dynamic programming approach constant space... This has a greedy vibe.

track:
cur_sum (0), max_sum (-inf)

if your current sum every goes below 0, set it to 0
if your current sum is positive, keep it

Complexity:
time: O(n) -> iterate through all nums
space: O(1) -> only store max_sum, cur_sum
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)

            if curr_sum < 0:
                curr_sum = 0

        return int(max_sum)
