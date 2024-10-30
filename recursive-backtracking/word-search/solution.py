"""
Given an `m x n` gird of characters `board` and a string `word`, return `true` if
`word` exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where
adjacent cells are horizontally or vertically neighboring. The same letter cell
may not be used more than once.

Example 1:

Input:

board = [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]

word = "ABCCED"
Output = True

|-------------------------------|
|   A X |   B X |   C X |   E   |
|-------------------------------|
|   S   |   F   |   C X |   S   |
|-------------------------------|
|   A   |   D X |   E X |   E   |
|-------------------------------|

Solution:
base cases:
- if i == word_length -> return True
- if board[x][y] != word[i] -> return False

Check all adjacent cells of board[x][y] and do a DFS (recursive backtrack)
until the soution is found. (be sure to MARK selected cell, and reset after backtracking.

Complexity:

Time:  O((m*n)**2) -> for each m*n positions, you could visit the whole vist. (this simplified from O(m*n * m*n).

Space: n -> length of the word

"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        width = len(board)
        height = len(board[0])
        word_length = len(word)

        # edge case
        if width == 1 and height == 1:
            return board[0][0] == word

        def backtrack(position, i):
            x, y = position
            # base case (if we have gotten to the end of the word)

            if i == word_length:
                return True

            # if the character is not the character that we are currently looking for
            if board[x][y] != word[i]:
                return False

            # this is in our path, so we mark it and create a temp var
            temp_char = board[x][y]
            board[x][y] = "#"

            # we now check every option from board[i][j] (up, down, left, right)
            # (0, 1): move column right by one (CHECK GRID RIGHT)
            # (1, 0): move row down by one (CHECK GRID DOWN)
            # (0,-1): move column left by one (CHECK GRID LEFT)
            # (-1,0): move row up by one (CHECK GRID UP)
            for x_offset, y_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                # calculate our new values with offsets
                new_x, new_y = x + x_offset, y + y_offset

                # validate we are in bounds
                if 0 <= new_x < width and 0 <= new_y < height:
                    if backtrack((new_x, new_y), i + 1):
                        return True

            # we did not find a valid path: reset board and get rid of #
            board[x][y] = temp_char
            return False

        # try each position in the grid
        for x in range(width):
            for y in range(height):
                # index 0 (starting at first letter)
                if backtrack((x, y), 0):
                    return True

        return False
