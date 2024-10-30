"""
You are given an m x n binary matrix grid. An island is a grou of 1's
(representing land) connected 4-directionally (horizontal and vertical).
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example:
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

Output: 6
The max island size is 6.

Solution:
- use a DFS to traverse each grid[x][y] that is a 1
- in our DFS call, when there is an adjacent valid grid available to travel to, we add +1
  to the traversal
- outside of the dfs, we take the max of the biggest area we have seen so far, vs whatever
  the dfs of grid[x][y] returns.

Complexity:
- Time is O(m * n) --> we need to check every index of grid[x][y] which is m length and n width
- Space is O(m * n) -> recursive callstack of dfs can be n * m in worse case
"""

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != 1:
                return 0
            else:
                grid[x][y] = 0
                return 1 + dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y + 1) + dfs(x, y - 1)

        max_area = 0

        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    max_area = max(max_area, dfs(x, y))

        return max_area
