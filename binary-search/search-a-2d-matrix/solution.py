"""
You are given an m by n integer matrix 'matrix' with the following two
properties:

- each row is sorted in non-decreasing order.
        - this can get us to O(m log n) --> because we can just use a binary search on reach row

- the first integer of each row is greater than the last integer of the previous row.
    (meaning that the last int in a row is SMALLER than the first int in the next row)
        - to remove the rows, would be O(log m) by removing the rows we don't need to search
        - combined with the above method, we can get to O(log m + log n)


Given an integer 'target', return 'true' if 'target' is in 'matrix' or 'false'
otherwise.

You must write a solution in O(log(m * n)) time copmlexity.

brute force: O(n * m)
- search every index


optimal solution:
- binary search the columns (considering the largest value in each row)
- binary search the r

"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1

        # look for target row (or target row does not exist)
        while top <= bottom:
            # compute middle row
            row = (top + bottom) // 2
            # if target is greater than the largest value in the row, we need to look upwards (SEARCH ONE ROW ABOVE)
            # REMEMBER: WE ARE RECOMPUTING THE MIDDLE ROW EACH TIME, THIS IS EFFECTIVELY CUTTING OUT HALF THE ROWS
            if target > matrix[row][-1]:
                top = row + 1
            # if the target value is less than the smallest value in the row, we need to look downwards (SEARCH ONE ROW BELOW)
            elif target < matrix[row][0]:
                bottom = row - 1
            # target value falls in current row
            else:
                break

        # now to do second portion of search (search the row)
        # if none of the rows contain target value
        if not (top <= bottom):
            return False

        # this is the row we want to search
        row = (top + bottom) // 2
        left = 0
        right = cols - 1

        while left <= right:
            middle = (left + right) // 2

            # search to the right (target is too big)
            if target > matrix[row][middle]:
                left = middle + 1
            # search to the left (target is too big)
            elif target < matrix[row][middle]:
                right = middle - 1
            # values match!
            else:
                return True
        return False
