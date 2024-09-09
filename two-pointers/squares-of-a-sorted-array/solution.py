from typing import List

"""
given an integer array nums sorted in non-decreasing order, return an
array of the squares of each number sorted in non-decreasing order.
    note: non-decreasing means that there may be a case of [1, 2, 2, 3]

    
Sample:
nums = [-4, -1, 0, 3, 10]
output: [0, 1, 9, 16, 100]

squaring nums: [16, 1, 0, 9, 100]
sorting: [0, 1, 16, 100]

solution:
- for num in nums, square each number (O(n)) time
- sort the array O(n long n)

time complexity: O(n log n) NOT GOOD ENOUGH


To achieve O(n) time -> use two-pointers technique

- create a pointer at leftmost and rightmost indexes of the array
- compare each value, take the squared result that is the larger of the 2 numbers, and assign to the end of our result array (this is guaranteed to be the largest value)
- shift the pointer whos value was selected, and move it inwards to the next value
- repeat until the pointers intersect
- return resulting array

time: O(n)
space: O(n) (the resulting array)
"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []

        left = 0
        right = len(nums) - 1

        # run until pointers meet (left is less than right so once l becomes greater than r, do not run)
        while left <= right:
            if nums[left] * nums[left] > nums[right] * nums[right]:
                res.append(nums[left] * nums[left])
                left += 1
            else:
                res.append(nums[right] * nums[right])
                right -= 1

        # reverse the array
        return res[::-1]
