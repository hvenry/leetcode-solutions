"""
You are given an integer array nums and an integer k. Find the maximum subarray sum
of all the subarrays of nums that meet the following conditions.

- The length of the subarray is k, and
- All the elements of the subarray are distinct

Return the maximum subarray sum of all the subarrays taht meet the conditions. If no subarray
meets the conditions, return 0.

A subarray is contiguous non-empty sequence of elements within an array.

Example:
nums = [1, 5, 4, 2, 9, 9, 9]
k = 3
output: 15

The valid subarrays of lenght 3 are:
- [1, 5, 4] -> sum = 10
- [5, 4, 2] -> sum = 11
- [4, 2, 9] -> sum = 15
- [2, 9, 9] -> invalid, repeating 9s
- [9, 9, 9] -> invalid, repeating 9s

Solution:
- use a sliding window of length k
- adjust sliding window such that all contents are unique, we can check that they are unique by using a hashmap

Slight Optimization:
- when the window is invald, we can move the ENTIRE window all the way over to the right, to skip adjusting of all subwindows with the duplicate

Complexity:
- Time: O(n)
- Space: O(n) -> prev_index can store at most n unique elemnts of nums
"""

from typing import List
# from collections import defaultdict


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cur_sum = 0
        max_sum = 0
        left = 0

        prev_index = {}

        for right in range(n):
            cur_sum += nums[right]
            i = prev_index.get(nums[right], -1)

            # make sure we have no duplicates
            while left <= i or right - left + 1 > k:
                cur_sum -= nums[left]
                left += 1

            if right - left + 1 == k:
                max_sum = max(max_sum, cur_sum)

            prev_index[nums[right]] = right

        return max_sum

        # Slightly less optimal approach (we do not skip over all windows with duplicates using index of duplcate)
        # n = len(nums)
        # cur_sum = 0
        # max_sum = 0
        # left = 0
        #
        # count = defaultdict(int)
        # for right in range(n):
        #     cur_sum += nums[right]
        #     count[nums[right]] += 1
        #
        #     if right - left + 1 > k:
        #         count[nums[left]] -= 1
        #         if count[nums[left]] == 0:
        #             count.pop(nums[left])
        #         cur_sum -= nums[left]
        #         left += 1
        #
        #     if len(count) == k and right - left + 1 == k:
        #         max_sum = max(max_sum, cur_sum)
        #
        # return max_sum
