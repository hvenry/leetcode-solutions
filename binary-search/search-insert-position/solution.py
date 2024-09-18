from typing import List

"""
given a sorted array of distinct integers and a target value, return the index
if the target is found. If not, return the index where it would be if it were
inserted in order.

solution:
- use binary search to locate index
- return left

why return left?
example:
target = 3
nums = [2]

L, R = 0, 0
Mid = (0 + 0) // 2

target is greater than middle, so left gets incremented by 1

returns left (because left <= right no longer holds), which is the correct insertion index.
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if target == nums[middle]:
                return middle
            # start searching to the right (target is bigger than middle)
            elif target > nums[middle]:
                left = middle + 1
            # start searching to the left (target is smaller than middle)
            else:
                right = middle - 1

        # we return left because left is always going to be on the side of the number where it should be indexed
        return left
