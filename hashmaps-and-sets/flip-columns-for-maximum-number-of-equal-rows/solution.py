"""
You are given an m x n binary matrix matrix.

You can choose any nubmer of columns in the matrix and flip every cell in that column (ie, change the
value of the cell from a 0 to 1 or vice versa).

Return the maximum number of rows that have all values equal after some number of flips.

Example 1:
matrix = [[0, 1], [1, 1]]
0 1
1 1
output: 1

After flipping no values, 1 row has all values equal.

Example 2:
matrix = [[0, 1], [1, 0]]
0 1
1 0
output: 2


After flipping values in the first column, both rows have equal values.

Solution:
- Use a counter.
- Standardize each row such that the first bit in it is 0.
- Convert each standardized row to a tuple to use as a key for the counter object.
- Do this for every row, and return the max of counter to get the maximum rows that could be the
  same after flipping values.

Complexity
- Time: O(m * n)
- Space: O(m * n)
"""

from collections import Counter
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # counter
        row_counter = Counter()

        for row in matrix:
            # keep rows starting with 0 the same, flip all values of rows that start with a 1
            standardized_row = tuple(row) if row[0] == 0 else tuple(1 - x for x in row)
            # increment the count using the key of the standardized rows
            row_counter[standardized_row] += 1

        # return the max count
        return max(row_counter.values())
