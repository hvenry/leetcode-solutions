"""
You are given a 0-indexed array nums and a non-negative integer k.

In one operation, you can do the following:
- Choose an index i that hasn't been chosen before from the range [0, nums.length - 1].
- Replace nums[i] with any integer from the range [nums[i] - k, nums[i] + ].

The beauty of the array is the length of the longest subsequence consisting of equal elements.
Return the maximum possible beauty of teh array nums after applying the operation any number of time.
- Note, you can only apply the operation at each index once.

A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none) without
changing the order of the remaining elements.

Example:
nums = [4, 6, 1, 2], k = 2
output: 3

- we can apply the operations on each index to get the array [4, 4, 1, 4], the total beauty is 3.

Solution:
- Sort the input array
- Use a sliding window approach to get the max length of numbers that are less than 2 * k apart
- return the max lenght, this is the maximum achievable beauty using 1 operation per index.

Complexity:
- Time: O(n log n)
- Space: O(1)
"""

from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        left = 0

        for right in range(n):
            # if this difference is greater than 2 * k, we shrink the window by moving left
            while nums[right] - nums[left] > 2 * k:
                left += 1

            # max of res or the current window lenght
            res = max(res, right - left + 1)

        return res
