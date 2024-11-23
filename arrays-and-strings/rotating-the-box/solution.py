"""
You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the
following:
- A stone '#'
- A stationary obstacle: '*'
- Empt '.'

The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity, Each stone falls down until
it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and
the inertia from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.

Example:
# . * .
# # * .

returns:
# .
# #
* *
. .

Solution:
- Go through each row, and then shift rocks as far left as possible by going through the reverse index of columns
    - Use a pointer to determine where you can move the current rock, increment it past any obstacles such that
      rocks do not fall past them
- After processing each row and shifting rocks down to as far left as possible, simply rotate the array and that
  is the solution

Complexity:
- Time: O(m * n)
- Space: O(m * n)
"""

from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        ROWS, COLS = len(box), len(box[0])

        for r in range(ROWS):
            # since we are going in reverse order, start i at len cols - 1
            i = COLS - 1
            for c in reversed(range(COLS)):
                # move stone over to valid index of col
                if box[r][c] == "#":
                    box[r][c], box[r][i] = box[r][i], box[r][c]
                    i -= 1
                # adjust i to start after obstacle
                elif box[r][c] == "*":
                    i = c - 1

        res = []
        # rotate answer 90 deg CW
        for c in range(COLS):
            col = []
            for r in reversed(range(ROWS)):
                col.append(box[r][c])
            res.append(col)

        return res
