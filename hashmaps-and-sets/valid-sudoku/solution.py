from typing import List

"""
Determine if a 9x9 Sudoku board is valid.
Only the filled cells need to be validated according to:
1. each row must contain digits 1-9 without repetition
2. each column must contain the digits 1-9 without repetition
3. each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition

hash set to detect if there are duplicates

use a hash set to check for duplicates in columns
use a hash set to check for duplicates in rows
use a hash set to check for duplicates in sub-boxes

to find the sub-box, we can use row // 3, col // 3 to get the sub-box [i, j] (which is [0, 0] to [2, 2])

"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        cols = set()
        subgrids = set()

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == ".":
                    continue

                # define unique keys to track seen numbers
                row_key = (i, num)
                col_key = (j, num)
                subgrid_key = (i // 3, j // 3, num)

                # see if number has already been seen
                if row_key in rows or col_key in cols or subgrid_key in subgrids:
                    return False

                # mark the keys as seen
                rows.add(row_key)
                cols.add(col_key)
                subgrids.add(subgrid_key)

        return True

    # time complexity is used to show how input grows - this is fixed so it is technically O(1)
