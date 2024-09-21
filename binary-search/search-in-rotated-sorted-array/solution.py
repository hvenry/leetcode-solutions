"""
There is an integer array num sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown
pivot index k (1 <= k < len(nums)) such that the resulting array is
[nums[k], nums[k+1], ... , nums[n-1], nums[0], nums[1], ... , nums[k-1]].

For example, [0, 1, 2, 4, 5, 6, 7] might be rotated at pivot index 3,
becoming: [4, 5, 6, 7, 0, 1, 2].

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

example:
nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Output: 4 (target is at index 4)

Solution:
- use binary search

Tricky part (review this)
Check if the left half is sorted:
- If nums[left] <= nums[middle], the left side is sorted.
- If the target is between nums[left] and nums[middle], search the left half by adjusting right.
- Otherwise, search the right half by adjusting left.

Check if the right half is sorted:
- If the left half is not sorted, the right side must be sorted.
- If the target is between nums[middle] and nums[right], search the right half by adjusting left.
- Otherwise, search the left half by adjusting right.

Return -1 if the target is not found after searching.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            # case 1, middle is target, return middle
            if target == nums[middle]:
                return middle

            # case 2, left sorted portion, check if the left half is sorted
            if nums[left] <= nums[middle]:
                if target > nums[middle] or target < nums[left]:
                    left = middle + 1
                else:
                    right = middle - 1

            # case 3, the right half must be sorted
            else:
                if target < nums[middle] or target > nums[right]:
                    right = middle - 1
                # target is greater than middle value, target is less than right value: search right
                else:
                    left = middle + 1

        return -1
