"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much
water it can trap after raining.

Example:
height          = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
output: 6
              #
      # . . . # # . #
  # . # # . # # # # # #
0 1 0 2 1 0 1 3 2 1 2 1

6 units of rain water '.' can fit between the elevation mapping of this height,

Solution:
- Use two-pointers set at left and right
- Keep track of max_left, max_right
- Shift pointer with smaller max value
    - Find the new max value of the pointer ( max(direction_max, height[direction]) )
    - Calculate max_direction - height[direction] to get the water level
    - Increase res by max - height[direction] -> this is how we keep track of all the water

Visualization (we do this using constant space):
max_right       = [3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 0]
max_left        = [0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]

min(l,r)        = [0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 1, 0]
min(l,r - h[i]) = [0, 0, 1, 0, 1, 2, 1, 0, 0, 1, 0, 0] = 6

Complexity:
- Time: O(n)
- Space: O(1)
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        res = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                res += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                res += right_max - height[right]

        return res
