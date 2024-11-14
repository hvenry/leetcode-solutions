"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are
adjacent, with the colors in the order red, white, and blue.

We will use integers 0, 1, and 2, to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example:
nums = [2, 0, 2, 1, 1, 0]
output nums = [0, 0, 1, 1, 2, 2]

Example 2:
nums = [2, 0, 1]
output nums = [0, 1, 2]

Solution:
- we store counts that is of lenght k, starting at [0, 0, 0]
- at index i, we count the number that we are seeing to the counts array (ie if i.val = 1, then counts = [0, 1, 0]
- we then reconstruct the array with the regions of each count

Counting Sort: O(n + k) where k is the range of data

Complexity:
    Time: O(n + k), k is 3 so this reduces to O(n)
    Space: O(k), same as above, so this reduces to O(1)
"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Do not return anything, modify nums in-place instead.
        counts = [0, 0, 0]

        for color in nums:
            counts[color] += 1

        # python unpacking
        R, W, B = counts

        # remmeber, inclusive : exclusive
        nums[:R] = [0] * R
        nums[R : R + W] = [1] * W
        nums[R + W :] = [2] * B
