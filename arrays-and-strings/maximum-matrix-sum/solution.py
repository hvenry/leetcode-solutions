"""
You are given an n x m integer matrix. You can do the following operation any number of times:

- Choose any two adjacent elements of matrix and multiply each of them by -1.

Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements
using the operation mentioned above.

Example 1:
matrix = [[1, -1], [-1, 1]]
returns: 4

- we can make all the numbers positive

Example 2:
matrix = [[1, 2, 3], [-1, -2, -3], [1, 2, 3]]
returns: 16

- we can make all but -1 positive.

Solution:
- This question requires a bit of thinking, initially I though this was a backtracking problem, but the answer is much
  more simpler that that.
- With the operation we are allowed to do on the matrix for this question, we are able to make all the numbers in the
  grid positive if the number of negatives is even, and we can make all but 1 positive if all the number of negatives is odd.

- Knowing this, we can simply keep track of total negatives, the min value, and the sum of matrix, if the number of negatives
  is even, return the matrix sum, if the number of negatives is odd, return the sum minus the absolute value of the min value
  * 2, because we need to negate the value of it, and then subtract it.

Complexity:
- Time: O(n^2)
- Space: O(1)
"""

from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        res = 0
        negatives = 0

        min_val = float("inf")

        for i in range(n):
            for j in range(n):
                cur_val = matrix[i][j]
                # track abs of the sum, we will be adjusting this based on number of negatives
                res += abs(cur_val)

                min_val = min(min_val, abs(cur_val))

                if cur_val < 0:
                    negatives += 1

        # we can use bitwise operator & to see if odd (last binary bit value of odd numbers == 1, even numbers == 0)
        if negatives & 1 and n > 1:
            res -= 2 * min_val

        return int(res)
