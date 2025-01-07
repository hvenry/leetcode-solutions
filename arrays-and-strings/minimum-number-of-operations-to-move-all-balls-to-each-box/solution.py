"""
You have n boxes. You are given a binary string boxes of length n, where boxes[i] is 0 if the ith box is empty, and
1 if it contains one ball.

In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1.
Note that after doing so, there may be more than one ball in some boxes.

Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to
the ith box.

Each answer[i] is calculated considering the initial state of the boxes.

Example:
boxes = "110"
returns: [1, 1, 3]

- Box 1: Takes 1 move to get every ball into it
- Box 2: Takes 1 move to get every ball into it
- Box 3: Takes 3 moves (2 for ball at index 0, 1 for ball at index 1) to get every ball into it.

Brute Force Approach:
- n^2 solution, use a double for loop using i and j to calculate the absolute value (distance) between j - i, if there
  is a ball at the index

Optimal Solution:
- Use a left and right pass to calculate the total moves

example:
balls = "001011"
res = [0, 0, 0, 1, 2, 4] -> we can get each index using a prefix sum of balls, moves

- now we do the same thing going backwards (right to left)
res = [11, 8, 5, 4, 3]

Complexity:
- Time: O(n)
- Space: O(n)
"""

from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * n

        balls, moves = 0, 0

        for i in range(n):
            res[i] = balls + moves
            # update balls and moves
            moves = moves + balls
            balls += int(boxes[i])

        balls, moves = 0, 0
        for i in reversed(range(n)):
            res[i] += balls + moves
            moves = moves + balls
            balls += int(boxes[i])

        return res

    # def minOperationsBrute(self, boxes: str) -> List[int]:
    #     n = len(boxes)
    #     res = [0] * n
    #
    #     for i in range(n):
    #         if boxes[i] == "1":
    #             for j in range(n):
    #                 res[j] += abs(j - i)
    #
    #     return res
    #
