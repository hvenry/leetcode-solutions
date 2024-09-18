from typing import List


"""
given an array fo integers 'nums' which is sorted in ascending order, and
an integer 'target', write a function to search 'target' in 'nums'.

if 'target' exists, then return its index. otherwise, return -1.

to implement this with O (log n) time complexity, use binary search.


how to implement
- if target is smaller than mid, search lef
- if target is larger than mid, search right
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            # check if target is at middle
            if target == nums[middle]:
                return middle
            # if target is smaller, ignore right half (set right to be middle THIS MOVES RIGHT HALFWAY INWARD)
            elif target < nums[middle]:
                right = middle - 1
            # if target is greater, ignore left half (set left to be middle THIS MOVES LEFT HALFWAY INWARD)
            else:
                left = middle + 1

        return -1
