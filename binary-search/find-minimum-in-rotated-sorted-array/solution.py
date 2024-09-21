"""
Suppose an array of length 'n' sorted in ascending order is rotated
between 1 and n times. For example, the array nums = [0, 1, 2, 4, 5, 6, 7]
might become
- [4, 5, 6, 7, 0, 1, 2] if it was rotated 4 times
- [0, 1, 2, 4, 5, 6, 7] if it was rotated 7 times

Notice that rotating an array [a[0], a[1], a[2], ... , a[n-1]] 1 time
results in teh array [a[n-1], a[0], a[1], a[2], ... a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum
element of this array.

example:
input = nums [3, 4, 5, 1, 2]
output: 1

explanation: the original array was [1, 2, 3, 4, 5] rotated 3 times

solution for O(log n): Binary search

- do binary search
- check if nums[middle] is >= nums[left]
    - if True, that means that the middle value is a part of the left sorted portion
        ie [3, 4, 5, 1, 2] where middle is 5, 5 >= 3, so we want to look at the RIGHT portion (to find 1)


    - if False, our middle value is part of the right sorted portion
        opposite case of above, so we search left
        ie [5, 1, 2, 3, 4] where middle is 2, 2 is not >= 5, so we want to check LEFT (to find 1)
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        left = 0
        right = len(nums) - 1

        while left <= right:
            # if we get to an array where it is already sorted (left is less than right)
            # this means we are in a completely ascending array, we want to return the smaller of the leftmost value or min
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break

            # if the array is not sorted, binary search time
            middle = (left + right) // 2
            res = min(res, nums[middle])

            # this is a part of the left sorted portion
            # search the right
            if nums[middle] >= nums[left]:
                left = middle + 1
            # search the left
            else:
                right = middle - 1

        return res
