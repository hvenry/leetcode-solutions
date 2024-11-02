"""
There is an m x n rectangular island that borders both the Pacific Ocean and
Atlantic Ocean. The Pacific Ocean touches the island's left and top edges,
and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are givenan m x n
interger matrix heights where heights[r][c] represents the height above sea
level of the cell at coordinate (r, c).

The island recieves a lot of rain, and the rain water can flow to neighbouring
cells directly north, south, east, and west if the neighbouring cell's height
is less than or equal to the current cell's height. Water can flow from any
cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [r_i, c_i] denotes
that rain water can flow from cell (r_i, r_i) to both the Pacific and Atlantic
oceans.

Example 1:
 -Pacific Ocean-------
|    1   2   2   3   5    |
|    3   2   3   4   4    |
|    2   4   5   3   1    |
|    6   7   1   4   5    |
|    5   1   1   2   4    |
     ------Atlantic Ocean-

Inputs:
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
result = [[0,4], [1,3], [1,4], [2,2], [3,0], [3,1], [4,0]]

Explanation:
[0,4]: [0,4] -> Pacific Ocean
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean
       [1,3] -> [1,4] -> Atlantic Ocean
... etc etc

Solutoin:
for every node in the grid, do a dfs marking the node as seen and we can only move forward if:
- the node next to it is less than the current node

we also need a return case, if the water gets to both side of the ocean

[0, 0] -> [0, -1] (pacific ocean)
[0, 0] -> [-1, 0] (pacific ocean)
[0, 0] -> [m, 0] (atlantic ocean)
[0, 0] -> [0, m] (atlantic ocean)

Solution:
- to make more sense conceptually, we will use a BFS to show how water flows
- we can just do 2 bfs's (1 for pacific and one for atlantic)

We should build up 2 sets of positions (to detect if you are in pacific or atlantic ocean cells)
- we construct a hashset to respresent the cells that water needs to reach to be put in pacitic and atlantic ocean
  this hashet is just the outermost layer of the:
    - Leftmost column and the Top column for Pacific
    - Rightmost column and the bottom column for Atlantic

We then take the intesection of the sets P and A to figure out when water can reach both sides.

Complexity:
Time: O(m * n) -> we need to check every point and add them to seen
Space: O(m * n) -> queue size can be at most n * m
"""

from typing import List
from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_que = deque()
        pacific_seen = set()

        atlantic_que = deque()
        atlantic_seen = set()

        rows = len(heights)
        cols = len(heights[0])

        # pacific ocean top row
        for y in range(cols):
            pacific_que.append((0, y))
            pacific_seen.add((0, y))

        # pacific ocean left column
        for x in range(1, rows):
            pacific_que.append((x, 0))
            pacific_seen.add((x, 0))

        # atlantic right wall (cols - 1 is fixed at last column)
        for x in range(rows):
            atlantic_que.append((x, cols - 1))
            atlantic_seen.add((x, rows - 1))

        # atlantic bottom wall (rows -1 is fixed at last row)
        for y in range(cols):
            atlantic_que.append((rows - 1, y))
            atlantic_seen.add((rows - 1, y))

        def get_coords(que, seen):
            while que:
                x, y = que.popleft()

                for x_off, y_off in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    new_x, new_y = x + x_off, y + y_off

                    # check if new_x is inbound row-wise
                    # check if new_y is inbound column-wise
                    # check if the value at new position [new_x][new_y] is greater than [x][y]
                    # check if we have not already seen this point [new_x][new_y]
                    if (
                        0 <= new_x < rows
                        and 0 <= new_y < cols
                        and heights[new_x][new_y] >= heights[x][y]
                        and (new_x, new_y) not in seen
                    ):
                        seen.add((new_x, new_y))
                        que.append((new_x, new_y))

        # get the coordinates of both the pacific and atlantic
        get_coords(pacific_que, pacific_seen)
        get_coords(atlantic_que, atlantic_seen)

        # Now we take the intersection
        return list(pacific_seen.intersection(atlantic_seen))
