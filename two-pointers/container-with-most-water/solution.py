"""
You are given an integer array height of length n. There are n vertical lines drawn such the two endpoints
of the ith line are (i, 0) and (i, height[i])).

Find the two lines that together with the x-axis form a container, such that it contains the most water.

Example:
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

  |         #
  |         #   |
  | #       #   |
  | #   #   #   |
  | #   # # #   |
  | #   # # # # |
  | # # # # # # |
# | # # # # # # |
  ^             ^

ans = 49

This is because 7 * 7 = 49, it takes the two walls, height[1] = 8, and height[8] = 7.

Solution:
- Use two-pointers, left starting at start at height[0] and right starting at height[len(height) - 1]
- find the width between both walls (right - left), and multiple by the min of left and right heights to get the current area
- update max area accordingly
- move left or right depending on which wall is shorter

Complexity
- Time: O(n)
- Space: O(1) -> we do not store anything for this solution
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        max_area = 0

        while left < right:
            width = right - left
            current_area = min(height[left], height[right]) * width
            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
