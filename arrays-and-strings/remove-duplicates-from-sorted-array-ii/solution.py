"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique
element appears at most twice. The relative order of the elements should be kept the same.

The result must be placed in the first part of the array nums. If there are k elements after removing the duplicates,
then the first k elements of nums hsould hold the final result. It does not matter what you leave beyond the first k
elements.

Return k after placing the final result in the first k slots of nums.

Example 1:
intput: nums = [1, 1, 1, 2, 2, 3]
output: nums = [1, 1, 2, 2, 3, _]
returns: 5

Solution:
- use two pointers i, j to start at index 1
    - i is used for scanning
    - j is used for writing
- we also use a counter to check if we have seen a number 2 times

- when counter is less than or equal 2, we move i and j up the list.
    - when counter is greater than 2, we move up j until we find a unique value
    - when a unique value is found, we set counter to 1 (used value), put the unique value in j's position, and move j forward

- we then go back to moving i an d j up the list until the condition of counter being greater than 2 is met

Start: count = 1
[0, 0, 0, 1]
    i
    j

1: count = 2
[0, 0, 0, 1]
       i
       j

2: count = 3: count gets updated to 3, larger than 2 so j does not move, we now move i to unique position, leaving j behind
[0, 0, 0, 1]
          i
       j

3: count = 1: 1 is unique, count set to 1, j is now moved
[0, 0, 1, 1]
          i
          j


Complexity:
- Time: O(n)
- Space: O(1)
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        count = 1
        n = len(nums)

        for i in range(1, n):
            # number not unique
            if nums[i] == nums[i - 1]:
                count += 1
            # number now is unique
            else:
                count = 1

            # move j up
            if count <= 2:
                nums[j] = nums[i]
                j += 1

        return j
