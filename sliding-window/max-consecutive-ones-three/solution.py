"""
Given a binary array nums and an integer k, return the maximum number of
consecutive 1's in the array if you can flip at most k 0's

(flipping meaning switching from 0 to 1)
ie k = 2, you can switch 2 0's in the array to 1 to make a longer consecutive sequence.

example:
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2

output: 6

explanation :[1, 1, 1, 0, 0, <1>, 1, 1, 1, 1, <1>]
(where <1> is a flipped 0)

solution:
- sliding window approach

O(n), only check each index once.
"""

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_length_window = 0
        num_zeros = 0
        left = 0

        # right slides the window forward finding a sequence of 1s
        for right in range(len(nums)):
            # 'flip' zero
            if nums[right] == 0:
                num_zeros += 1

            # window is invalid condition (no more zeros to flip), slide the window from the left side
            while num_zeros > k:
                if nums[left] == 0:
                    # decrement this value if we are removing a 'flipped' zero
                    num_zeros -= 1
                left += 1

            max_length_window = max(max_length_window, (right - left + 1))

        return max_length_window
