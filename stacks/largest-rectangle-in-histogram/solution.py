"""
Given an array of integers heights representing the histogram's bar height where the width of
each bar is 1, return the area of the largest rectangle in the histogram.

Example:
heights = [2, 1, 5, 6, 2, 3]
output: 10:

The rectangles 5 and 6 beside each other produce the largest rectangle area of 5*2 = 10.

Solution:
1.
- use a stack to push values as (height, index), keep track of max area
2.
- while sthe stack is not empty, we pop the top tuple (height, j),
    - we can calculate the width as i - j (current index minu the index of the popped tuple)
    - we compute the area as height * width, and update the max area
    - we update start to equal to j, to extend the starting point of the rectangle
3.
- we then process the remaining stack
    - pop (height, j) and calculate n - j (since rectangle can extend to end of histogram)
    - compute the area and update max width

The stack makes sure that every height popped is processed for the larges possible rectangle.

Visualization for [2, 1, 5, 6, 2, 3]
1. Start with an empty stack [], max_area = 0

2. process heights
- index 0: push (2, 0)                                          stack = [(2, 0)]
- index 1: pop (2, 0), calculate area 2 * 1 = 2, push (1, 0)    stack = [(1, 0)] <- popped becuase 2 > 1
- index 2: push (5, 2)                                          stack = [(1, 0), (5, 2)]
- index 3: push (6, 3)                                          stack = [(1, 0), (5, 2), (6, 3)]
- index 4: pop (6, 3) and (5, 2), calculate areas 6*1=6,
           5*2 = 10, push (2, 2)                                stack = [(1, 0), (2, 2)] <- popped because 6 > 5
- index 5: push (3, 5)                                          stack = [(1, 0), (2, 2), (3, 5)]

3. process remaining stack
- pop (3, 5), area = 3*1=3
- pop (2, 2), area = 2*4=8
- pop (1, 0), area = 1*6=6

max area is 10.

Complexity:
- Time: O(n)
- Space: O(n)
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            start = i

            # take off candidates when current height is less than the height of the element at the top of the stack
            while stack and height < stack[-1][0]:
                h, j = stack.pop()
                # this is the width of the current rectangle
                width = i - j
                area = h * width
                max_area = max(max_area, area)
                # update starting index to the index of the popped bar
                start = j

            stack.append((height, start))

        # process the remainder of the stack (check if any area is greater than max area):w
        while stack:
            height, j = stack.pop()
            width = n - j
            area = height * width
            max_area = max(max_area, area)

        return max_area
