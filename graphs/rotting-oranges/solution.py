"""
You are given an m x n grid where each cell can have one of three values:
- 0 representing an empy cell
- 1 representing a fresh orange
- 2 representing a rotten orange

Every minute, any fresh orange that is 4-directionally adjacent to a rotten
orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.
If this is impossible, return -1

Example:
Grid = [[2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]]

Output: 4

Minute 1
Grid = [[2, 2, 1],
        [2, 1, 0],
        [0, 1, 1]]

Minute 2
Grid = [[2, 2, 2],
        [2, 2, 0],
        [0, 1, 1]]

Minute 3
Grid = [[2, 2, 2],
        [2, 2, 0],
        [0, 2, 1]]

Minute 4
Grid = [[2, 2, 2],
        [2, 2, 0],
        [0, 2, 4]]

All oranges rotten in 4 minutes.

Solution
- calculate the amount of fresh oranges

- Use a bfs and implement it with a deque
- process the queue in rounds to calculate how many minutes (each round, add +1 to minutes)

- check for surrounding fresh oranges, if we find one, add it to the queue and set to ROTTON
  and also subtrack 1 from the count of fresh oranges

- keep exploring via dfs until there is no more queue
- if the amount of fresh oranges = 0, return the number of minutes it took
- if the amount of fresh oranges != 0, return -1
"""

from typing import List
from collections import deque


class Soluion:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        FRESH = 1
        ROTTEN = 2

        num_rows = len(grid)
        num_cols = len(grid[0])

        num_fresh = 0
        q = deque()

        # calculate number of fresh oranges, add rotten to the queue
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == ROTTEN:
                    q.append((row, col))

                elif grid[row][col] == FRESH:
                    num_fresh += 1

        if num_fresh == 0:
            return 0

        # we set this to -1 so that whe our final bfs that terminates the loop does not add an extra minut
        num_minutes = -1

        while q:
            # we want to chekc the bfs in rounds, so that each competed bfs of the current que adds +1 to minutes
            q_size = len(q)
            num_minutes += 1

            # go through every element in the current queue, and build up from there, once this terminates, a new queue will exist of newly expanded rotten oranges
            for _ in range(q_size):
                row, col = q.popleft()

                for new_row, new_col in [
                    (row, col + 1),
                    (row + 1, col),
                    (row, col - 1),
                    (row - 1, col),
                ]:
                    # verify position is in bounds
                    if (
                        0 <= new_row < num_rows
                        and 0 <= new_col < num_cols
                        and grid[new_row][new_col] == FRESH
                    ):
                        grid[new_row][new_col] = ROTTEN
                        num_fresh -= 1
                        q.append((new_row, new_col))

        # our return condition is if number of fresh is 0, we have rotted all oranges and now have the minutes to show for it, else return -1
        if num_fresh == 0:
            return num_minutes
        else:
            return -1
