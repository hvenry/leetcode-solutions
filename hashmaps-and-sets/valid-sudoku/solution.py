"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to
the following rules:

1. Each row must contain digits 1-9 without repetition
2. Each column must contain the digits 1-9 without repetition
3. Each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition

Note:
- A Sudoku board (partially filled) could be valid but it is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

Hash Set Solution:
- use a hash set to detect if there are duplicates
    - check for duplicates in columns
    - check for duplicates in rows
    - check for duplicates in sub-boxes
        - to find the sub-grid, we can use row // 3, col // 3 to get the sub-box [i, j] (which is [0, 0] to [2, 2])

Complexity (for a 9x9 board):
- Time: O(1) -> O(9 * 9  = 81)
- Space: O(1) -> O(3 * 81 = 243) -> comes from generating subgrids

Complexity (for an n*n board):
- Time: O(n^2)
- Space: O(n^2)

Optimal Solution: Use a bitmask


Complexity (for an board):
- Time: O(n^2) -> processing every cell
- Space: O(n) -> wow! bitmasks reduce space by root(n)
"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Optimal Solution (bitmask)
        # how to interpret bitmask: rows[0] bitmask is 0b001010101, meaning 1, 3, 5, 7
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                # convert the number from string to integer, and normalize to 0-indexed
                val = int(board[r][c]) - 1

                # calculate index of the 3x3 subgrid
                square_index = (r // 3) * 3 + (c // 3)

                # check if number has already been seen in the row, col, or subgrid (check bitmasks)
                # 1 << val shifts a 1 to the left by 'val' positions, & checks if the corresponding bit has been seen
                if (1 << val) & rows[r]:
                    return False
                if (1 << val) & cols[c]:
                    return False
                if (1 << val) & squares[square_index]:
                    return False

                # markd the numbers as seen in the row, col, and subgrid (update bitmasks)k
                # |= updates rows[r] to include the bit for val
                # Example
                # rows[r] is 0b001010101, val = 4, (1 << 4 = 0b0001000), then
                # rows[r] |= 0b00010000 = 0b001110101 -> this effectively adds it to the row
                rows[r] |= 1 << val
                cols[c] |= 1 << val
                squares[square_index] |= 1 << val

        return True

        # # our constant space 9x9 solution
        # rows = set()
        # cols = set()
        # subgrids = set()
        #
        # for i in range(9):
        #     for j in range(9):
        #         num = board[i][j]
        #
        #         if num == ".":
        #             continue
        #
        #         # define unique keys to track seen numbers
        #         row_key = (i, num)
        #         col_key = (j, num)
        #         subgrid_key = (i // 3, j // 3, num)
        #
        #         # see if number has already been seen
        #         if row_key in rows or col_key in cols or subgrid_key in subgrids:
        #             return False
        #
        #         # mark the keys as seen
        #         rows.add(row_key)
        #         cols.add(col_key)
        #         subgrids.add(subgrid_key)
        #
        # return True
