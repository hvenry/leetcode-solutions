"""
On a 2x3 board, there are five tiles labeled from 1 to t, and an empty square represented by 0. A move consists
of choosing 0 and 4-directionally adjacent number and swapping it.

The state of the board is solved if any only if the board is [[1, 2, 3], [4, 5, 6]].

Given the puzzle board, return the least number of moves required  so that the state of the board is solved. If it
is impossible, for the state of the board to be solved, return -1.

Example 1:
board = [[1, 2, 3], [4, 0, 5]]
returns: 1

- We can swap the 0 and the 5 in one move to solve the puzzle.

Example 2:
board = [[1, 2, 3], [5, 4, 0]]
returns: -1

- There are no possible moves to make the board solved.

Solution:
- Map the problem to a string, ie board [[1, 2, 3], [4, 0, 5]] turns into "123405"
- We can create an adjacecy list to show possible moves between indicies, for instance, index 0 can move to index 1, 3.
- Use a BFS to explore the adjaceny list of the graph to see if it is possible to find a solution.

Complexity:
- Time: O(m + n)!
- Space: O(m + n)!
"""

from typing import List
from collections import deque


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        adjacent = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4],
        }

        # Board
        b = "".join([str(c) for row in board for c in row])

        # q for BFS
        q = deque([(b.index("0"), b, 0)])  # stores (i, board, length)

        visited = set([b])

        while q:
            i, b, length = q.popleft()

            # desired state
            if b == "123450":
                return length

            # convert to list
            b_arr = list(b)

            # go through neighbors in adjacency list
            for neighbor in adjacent[i]:
                new_b_arr = b_arr.copy()
                new_b_arr[i], new_b_arr[neighbor] = b_arr[neighbor], b_arr[i]
                new_b = "".join(new_b_arr)

                if new_b not in visited:
                    q.append((neighbor, new_b, length + 1))
                    visited.add(new_b)

        return -1
