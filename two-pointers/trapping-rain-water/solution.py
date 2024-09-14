from typing import List

"""
given n non-negative integers representing an elevation map where the width
of each bar is 1, compute how much water it can trap after raining.

example:
height          = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
max_right       = [3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 0]
max_left        = [0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
min(l,r)        = [0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 1, 0]
min(l,r - h[i]) = [0, 0, 1, 0, 1, 2, 1, 0, 0, 1, 0, 0] = 6

output: 6

6 units of rain water can fit between the elevation mapping of this height,
for instance, 1 unit of rain water can fit between height[1] and height[2], because
there is two walls with the minimum height being 1, that can store 1 unit of rain water.


** IMPORTANT TO UNDERSTAND **
how to calculate water per index: find min(left[i], right[i]) and subtract it from height[i]
- see example solution


How to optimize this for O(1) space instead of O(n)?
solution: use two-pointers approach
- set left and right pointers
- set left and right max to height of left and right
- set res to 0

- while the left and right pointers have not intersected
- check which max is greater, increment the pointer of which is greater, and adjust max accordingly
- calculate there result (which he have proved above is [left or right]max - height[left or right])

return result

key understanding
- why max - height max is equal to the water that can be stored
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        # edge case
        if not height:
            return 0

        left = 0
        right = len(height) - 1

        left_max = height[left]
        right_max = height[right]

        res = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                # this can't be negative because the max is always going to be 0 or more
                res += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                res += right_max - height[right]

        return res
