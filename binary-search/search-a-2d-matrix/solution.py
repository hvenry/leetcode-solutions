"""
You are given an m by n integer matrix 'matrix' with the following two properties:
- Each row is sorted in non-decreasing order
- The first integer of each row is greater than the last integer of the previous row

Given an integer target, return true if target is in matrix or False otherwise.

Example:
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]

1  3  5  7
10 11 16 20
23 30 34 60

target = 3
returns: True -> we can find 3 in matrix.

Solution:
- binary search the columns using top and bottom of matrix to find the row to search
- binary search the resulting row (if top <= bottom) to see if the value is in it, return True if found

Complexity:
- Time: O(log(n * m))
- Space: O(1)
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # One pass solution (flatten array), treat as 1D search space and calculate 2D indicies
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n - 1

        while left <= right:
            mid = (left + right) // 2

            # row index
            i = mid // n
            # column index
            j = mid % n

            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                left = mid + 1
            else:
                right = mid - 1

        return False

        # rows = len(matrix)
        # cols = len(matrix[0])
        # top = 0
        # bottom = rows - 1
        #
        # # look for target row (or target row does not exist)
        # while top <= bottom:
        #     row = (top + bottom) // 2
        #     if target > matrix[row][-1]:
        #         top = row + 1
        #     elif target < matrix[row][0]:
        #         bottom = row - 1
        #     else:
        #         break
        #
        # if not (top <= bottom):
        #     return False
        #
        # row = (top + bottom) // 2
        # left = 0
        # right = cols - 1
        #
        # while left <= right:
        #     middle = (left + right) // 2
        #     if target > matrix[row][middle]:
        #         left = middle + 1
        #     elif target < matrix[row][middle]:
        #         right = middle - 1
        #     else:
        #         return True
        # return False
