"""
You are given two integers m an n representing a 0-indexed m x n grid. You are also given two 2D integer arrays
guards and walls whre guards[i] = [row_i, col_i] and walls[j] = rows_j, cols_j] representing the positions of the ith
guard and jth wall respectively.

A guard can see every cell in four cardinal directions (north, east, south, or west) starting from their position unless
obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.

Return the number of unoccupied cells that are not guarded.

Example:
m = 4, n = 6
guards = [[0, 0], [1, 1], [2, 3]]
walls  = [[0, 1], [2, 2], [1, 4]]

Visualization (let guards = 1, walls = 2, guarded = 3, unguarded = 0):

1 2 0 3 0 0
3 1 3 3 2 0
3 3 2 1 3 3
3 3 0 3 0 0

    output: 7 (count 0s)

Example 2:
m = 3, n = 3
guards = [[1, 1]]
walls  = [[0, 1], [2, 2], [1, 4]]

Visualization:

0 2 0
2 1 2
0 2 0

    output: 4

Solution:
- Construct m * n grid of 0s
- mark any guards and walls on the grid
- go through every guarded index, and mark the LEFT, RIGHT (rows), UP, DOWN (cols) that are guarded

- iterate through the resulting grid, add +1 to a count for every 0 seen, return the count.

Complexity:
- Time: O(m * n +  G * (m + n)) -> G * (m + n) is the time it takes to mark all guarded cells
- Space: O(m * n)
"""

from typing import List


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        # construct grid of 0s
        grid = [[0] * n for _ in range(m)]

        # mark guards as 1, walls as 2
        for r, c in guards:
            grid[r][c] = 1
        for r, c in walls:
            grid[r][c] = 2

        def mark_guarded(r, c):
            # rows left to right
            for row in range(r + 1, m):
                # stop when we hit a guard (so we dont visit cells twice) or wall
                if grid[row][c] in [1, 2]:
                    break
                grid[row][c] = 3
            # rows right to left
            for row in reversed(range(0, r)):
                if grid[row][c] in [1, 2]:
                    break
                grid[row][c] = 3

            # cols top to bottom
            for col in range(c + 1, n):
                if grid[r][col] in [1, 2]:
                    break
                grid[r][col] = 3

            # cols bottom to top
            for col in reversed(range(0, c)):
                if grid[r][col] in [1, 2]:
                    break
                grid[r][col] = 3

        for r, c in guards:
            mark_guarded(r, c)

        res = 0

        # count how many cells remain unguarded (0)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    res += 1

        return res
