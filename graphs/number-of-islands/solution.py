"""
Givn an m x n 2D binary grid 'grid' which represents a map of 1's (land)
and 0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are
surrounded by water.

Example:
grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
Output: 1

(there is only 1 island)


Solution:
- Start a DFS traversal for each [i][j] cell in the grid that is 1 (land)
- set original cell to 0 and explore all adjacent cells, also setting them to 0

Complexity:
Time: O(m x n) -> we need to go to each cell
Space: O(n x m) ->  dfs recursive callstack is at most the entire grid
                    dfs iterative stack size it at most entire grid.
                    bfs queue length could be entire grid
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # dfs solution
        def dfs(x, y):
            # check if x or y value is out of bounds and if it is not a 1
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != "1":
                return
            else:
                grid[x][y] = "0"
                # go to the right (increase column)
                dfs(x, y + 1)
                # do left (decrease column)
                dfs(x, y - 1)
                # go down (increase row)
                dfs(x + 1, y)
                # go up (decrease row)
                dfs(x - 1, y)

        num_islands = 0

        # do a dfs on all cells that equal to 1
        for x in range(m):
            for y in range(n):
                if grid[x][y] == "1":
                    num_islands += 1
                    dfs(x, y)

        return num_islands
