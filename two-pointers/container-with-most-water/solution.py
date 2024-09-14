from typing import List

"""
you are given an integer array height of length n. There are n vertical lines drawn
such that two endpoints of the ith line are (i, 0) and (i, height[i]). (bottom of x axis to height value)

find the two lines that together with the x-axis form a container, such that it contains the most
water.

example:


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
ans = 49

this is because 7 * 7 = 49, it takes the two walls, height[1] = 8, and height[8] = 7



solution:
use two-pointers approach,
- start at height[0] and height[len(height) - 1]
- calculate the min of both ^2
- move the pointer up to the next largest wall ->


"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            current_area = min(height[left], height[right]) * width

            if current_area > max_area:
                max_area = current_area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
