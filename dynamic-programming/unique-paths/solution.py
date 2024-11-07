"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (ie grid[0][0]).

The robot tries to move to the bottom-right cornver (ie grid[m-1][n - 1]). The robot can only move either
down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths the robot can take to reach the
botom-right corner.

The test casts are generated so that the answer will be less than or equal to 2 * 10^9.

Example 1:
m = 3
n = 7

Output 28

for grid: m=3, n=7
1   1   1   1   1   1   1
1   2   3   4   5   6   7
1   3   6   10  15  21  28

Idea: the amount of ways to get to a grid index, is the sum of the grid index above it, and to the left of it.
    - For any out of bound position: add +0.

We can solve this with dp, using both the  top down and bottom up approach.

Solution (recurrence relation)

starting index (base case)
if i == j == 0: return 1

out of bounds:
return 0

else, we add up the cell above and cell to the left of current cell and return that
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # # 1. Recursive solution, with overlapping subproblems Time: O(2^(m*n)), Space: O(m*n)
        #
        # def paths(i, j):
        #     # at 0, 0 (one way to get here)
        #     if i == j == 0:
        #         return 1
        #     # out of bounds positions
        #     elif i < 0 or j < 0 or i == m or j == n:
        #         return 0
        #     else:
        #         # return the total amount of ways to get to 1 to the left + amount of ways to get to 1 above of the current cell
        #         return paths(i, j - 1) + paths(i - 1, j)
        #
        # return paths(m - 1, n - 1)

        # # 2. Top Down DP (Memoization), Time: O(m*n), space: O(m*n)
        # memo = {(0, 0): 1}
        #
        # def paths(i, j):
        #     if (i, j) in memo:
        #         return memo[(i, j)]
        #     elif i < 0 or j < 0 or i == m or j == n:
        #         return 0
        #     else:
        #         val = paths(i, j-1) + paths(i-1, j)
        #         memo[(i, j)] = val
        #         return val
        #
        # return paths(m-1, n-1)

        # 3. Bottomup DP (Tabulation)

        dp = []
        # construct n * m grid of 0
        for _ in range(m):
            dp.append([0] * n)

        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                # build up dp array
                val = 0
                if i > 0:
                    val += dp[i - 1][j]
                if j > 0:
                    val += dp[i][j - 1]

                dp[i][j] = val

        return dp[m - 1][n - 1]
