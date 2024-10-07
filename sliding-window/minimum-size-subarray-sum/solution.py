"""
Given an integer of positive integers nums and a positive integer target, return
the minimal length of a subarray whose sum is greater than or equal to target.
If there is no such subarray, return 0 instead.

Example 1:
target = 7
nums = [2, 3, 1, 2, 4, 3]
output: 2

The subarray [4, 3] has the minimal length.

Solution: sliding window


- initialize left pointer, a total sum, and a min length to track our results.
- for right in len(nums), we want to check if our sum is >= target
    (greater than is important, it means that our window meets the requirements of target)

- if our sum is less than target, we move the right pointer over
- once our condition is met of sum >= target, we can now set our min length to the min(min_length OR window length)
    (window length is found by taking right - left and adding 1, we add 1 because our first index is 0)
- next we move the left pointer over but before we do that we need to remove its value from our total sum
- repeat this process n times until right has reached the end of the array
"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total_sum = 0
        min_length = float("inf")
        left = 0

        for right in range(len(nums)):
            total_sum += nums[right]

            while total_sum >= target:
                min_length = min(min_length, right - left + 1)
                total_sum -= nums[left]
                left += 1

        return min_length if min_length < float("inf") else 0
