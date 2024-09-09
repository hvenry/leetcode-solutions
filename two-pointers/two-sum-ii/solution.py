from typing import List

"""
use two pointers technique to find the two indexes that add up
to our target sum in a sorted list

we can do this by assigning 2 pointers, one at index 0 (left) and one 
at the final index (right), and then shift them inside the array one at a
time.

we move the left pointer up the array if our sum needs to be larger
(since the array is increasing in size)

we move the right pointer down the array if our sum needs to be smaller
(same reason as above)

if the pointers intersect, return nothing
if target sum is reached, return index of left, and index of right.
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]

            if sum == target:
                return [left + 1, right + 1]

            # if sum < target: we want to increase it, by moving left pointer
            if sum < target:
                left += 1
            # else, if sum is >= target, we want to lower it by moving the right pointer
            else:
                right -= 1
