"""
You are given a 0-indexed integer array nums of length n.

nums contains a valid split at index i if the following are true:
- The sum of the first i + 1 elements is greater than or equal to the sum of the
  last n - i - 1 elements.
- There is at least one element to the right of i. That is, 0 <= i < n - 1

Return the number of valid splits in nums.

Example:
nums = [10, 4, -8, 7]
returns: 2

i = 0
- first part sum is 10, (nums[0] = 10)
- second part sum is 3 (nums[1] + nums[2] + nums[3] = 4 + -8 + 7 = 3)
- this is a valid split (10 >= 3)

i = 1
- first part sum is 14 (nums[0] + nums[1] = 10 + 4 = 14)
- second part sum is -1 (nums[2] + nums[3] = -8 + 7)
- this is a valid split (14 >= -1)

i = 2
- first part sum is 6
- second part sum is 7
- this is not a valid split (6 >= 7)

There are no more valid splits, return 2.

Solution:
- Get the total sum of all numbers in the nums
- For each number in nums, increment a current sum by the value of the current number,
  and decrement the total sum by the current number.
- If the sum on the left is greater than or equal the sum that is left order, increment
  the result by 1.

Complexity:
- Time: O(n)
- Space: O(1)
"""

from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        left_sum = 0
        right_sum = sum(nums)
        res = 0

        for i in range(n - 1):
            left_sum += nums[i]
            right_sum -= nums[i]

            if left_sum >= right_sum:
                res += 1

        return res
