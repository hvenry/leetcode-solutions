"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exacly one solution.

Example 1:
nums = [-1, 2, 1, -4]
target = 1
returns 2

The sum that is closest to the target is 2 (-1 + 2 + 1 = 2).

Example 2:
nums = [0, 0, 0]
target = 1
returns 0

The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

Solution:
- sort the array :)
- set a cloest value to infinity
- start at first index, and use the same two pointers technique from three-sum

target = 5
[-3, -3, -2, 0, 1, 2, 3]
  i   <--------------->
      left            right

- we keep track of a current sum (currently at -3 + -3 + 3 = -3)
- we then set our cloest value to this found -3
- we then adjust our left and right pointers to look for a better sum
- we set the new cloest_value to the minimum distance that we found from the target ( | target - sum | )

- to find all of our possible sums, we just move the i to the next unique position, and check the new space of left and right to
  find a new closest.

[-3, -3, -2, 0, 1, 2, 3]
          i  <--------->
             left     right

- if at any point, our closest = target, we just return that.

Complexity
- Time: O(n^2)
- Space: O(1) -> assuming sorting in place
"""

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = float("inf")

        for i in range(n):
            # find unique 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            # two pointers technique (fun fact: called a 'squeeze')
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]

                # check is we have a better distance at these values then we did before
                if abs(cur_sum - target) < abs(closest_sum - target):
                    closest_sum = cur_sum

                if cur_sum == target:
                    return target
                elif cur_sum < target:
                    left += 1
                else:
                    right -= 1

        return int(closest_sum)
