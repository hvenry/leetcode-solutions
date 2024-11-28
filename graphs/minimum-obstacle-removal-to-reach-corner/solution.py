"""
You ar egiven a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:
- 0 represents an empty cell.
- 1 represents an obstacle that may be removed.

You can move up, down, left, or right from and to an empty cell.

Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to
the lower right corner (m - 1, n - 1).

Example 1:
grid = [[0, 1, 1], [1, 1, 0], [1, 1, 0]]
returns 2

0 1 1    0 0 0
1 1 0 -> 1 1 0
1 1 0    1 1 0

- We can remove the obstacles at (0, 1) and (0, 2) to create a path from (0, 0) to (2, 2).

Solution:
- We can use a deque, and use a BFS to explore the grid.
- We will keep the deque in monotonic increasing order, such that cells that are unblocked are added to the
  left, and cells that are blocked are added to the end.
- Exploring the graph this way by using a deque, we can keep using unblocked cells until we abosoluetly
  need to remove an obstacle.
- When we need to remove an obstacle, there will be a 1 at the front of the deque, we then just add +1 to obstacles
  and continue on.
- By doing this, the next obstacles we face have a 2 value instad of a 1 value, (because 2 obstacles to use their position)
  and we can take advantage of that by putting their values at the end of the deque until we run out of 1s.
- When the current cell is matching the end cell, return the number of obstacles.

Complexity:
Time: O(m * n)
Space: O(m * n)
"""

from typing import List
from collections import deque


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        q = deque([(0, 0, 0)])
        # visit 0, 0 first
        visited = set([(0, 0)])

        while q:
            obstacles, r, c = q.popleft()

            # check if we are at the end
            if (r, c) == (ROWS - 1, COLS - 1):
                return obstacles

            neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]

            for nr, nc in neighbors:
                if (nr, nc) in visited or nr < 0 or nc < 0 or nc == COLS or nr == ROWS:
                    continue

                # this lets us maintain our monotonic increasing deque
                if grid[nr][nc] == 1:
                    q.append((obstacles + 1, nr, nc))
                else:
                    q.appendleft((obstacles, nr, nc))

                visited.add((nr, nc))
