"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two
numbers such that they add up to a specific target number. Let these two numbers be numbers[index_i]
and numbrs[index_2], where 1 <= index_1 < index_2 <= numbers.length.

Return the indices of the two numbers, index_1 and index_2 added by one as an integer [index_i, index_2]
of length 2.

There is always exactly 1 solution, you may not use the same element twice.

Example 1:
numbers = [2, 7, 11, 15]
target = 9
returns: [1, 2]

The sum of 2 and 7 is 9, therefore, index_1 = 1, index_2 = 2.

Example 2:
numbers = [2, 3 4]
target = 6
returns: [1, 3]

2 + 4 = 6.

Solution:
- Since array is sorted, use two pointers technique to find the two indexes that add up to our target sum in a sorted list.
- We can do this by assigning 2 pointers, one at index 0 (left) and one at the final index (right), and then shift them inside
  the array one at a time.
    - We move the left pointer up the array if our sum needs to be larger (we need to add larger numbers, we have not reached target)
    - We move the right pointer down the array if our sum needs to be smaller (we need to add smallers numbers, we overshot)

- if the pointers intersect, return nothing
- if target sum is reached, return index of left, and index of right.

Complexity:
    Time: O(n)
    Space: O(1)
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n - 1

        # go until our pointers intersect
        while left < right:
            sum = numbers[left] + numbers[right]

            if sum == target:
                return [left + 1, right + 1]
            elif sum < target:
                left += 1
            else:
                right -= 1

        return []
