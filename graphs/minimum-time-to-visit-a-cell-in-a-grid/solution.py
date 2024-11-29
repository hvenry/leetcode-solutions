"""
You are given a m x n matrix grid consisting of non-negative integers where grid[row][col] represents
the minimum time required to be able to visit the cell (row, col), which means you can visit the cell
(row, col) only when the time you visit it is greater than or equal to grid[row][col].

You are standing in the top-left cell of the matrix in the 0th second, and you must move to any adjacent
cell in the four directions: up, down, left, and right. Each move you make takes 1 second.

Return the minimum time required in which you can visit the bottom-right cell of the matrix. If you cannot
visit the bottom-right cell, then return -1.

Example 1:
grid = [[0, 1, 3, 2], [5, 1, 2, 5], [4, 3, 8, 6]]

0 1 3 2
5 1 2 5
4 3 8 6

returns 7

- t = 0, we are on cell (0, 0)
- t = 1, move to cell (0, 1) -> possible because grid[0][1] <= t
- t = 2, move to cell (1, 1)
- t = 3, move to cell (1, 2)
- t = 4, move to cell (1, 1)
- t = 5, move to cell (1, 2)
- t = 6, move to cell (1, 3)
- t = 7, move to cell (2, 3) -> this is the end, return 7

Solution:
- use Dijkstra algorithm, the graph is weighted by the time to move to each cell
- use a min-heap priority queue (heapq) to keep track of potential moves, ordered by earliest time they can be made
- check neighbors of current cell, find our how long it would take to make the move to each, add to heapq
    - there is a clever way to calculate time of STALLING (ie we go back and fourth to add extra time, adding + 1 to a wait var)
- keep going intilthe current cell is the bottom right of the grid (rows - 1, cols - 1)

Complexity:
- Time: O( (n * m) log(n * m) ) -> push of pop on heap takes O(log(n * m)), ad there are (n * m) cells
- Space: O(n * m) -> worst case we store all cells in the heap, which is O(n * m)
"""

from typing import List
import heapq


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        # base case (we cannot move)
        if min(grid[0][1], grid[1][0]) > 1:
            return -1

        min_heap = [(0, 0, 0)]
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        while min_heap:
            time, r, c = heapq.heappop(min_heap)

            # we have reached the end
            if (r, c) == (ROWS - 1, COLS - 1):
                return time

            # try possible neighbors
            neighbor = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for nr, nc in neighbor:
                # validate current neighbor
                if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or (nr, nc) in visited:
                    continue

                # find our timee to wait, we add extra wait time when we need to go back and forth
                wait = 0
                if abs(grid[nr][nc] - time) % 2 == 0:
                    wait = 1

                # we take the max time because we cannot go back in time
                next_time = max(grid[nr][nc] + wait, time + 1)
                heapq.heappush(min_heap, (next_time, nr, nc))

                visited.add((nr, nc))
