"""
You are given an interger array cost where cost[i] is the cost of i^th step on a staircase. Once you pay the cost,
you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example:
cost = [10, 15, 20]
output: 15

- You will start at index 1, pay 15 and climb two steps to reach the top.

If you start at 10 (index 0), you would have to pay 10 and can go either to 15 or 20, and then would need to pay to finish.

Solution:
Recurrence Relation:
- base cases: i=0 returns 0, i=1 returns 0
- we want to return the minimum of
    2 steps back: cost[i-2] + min_cost(i-2)
    1 step back: cost[i-1] + min_cost(i-1)

The best way to solve this problem is using a constant space bottom up approach.
"""

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # # Recurrence solution: O(2^n), NOT OPTIMAL
        # n = len(cost)
        #
        # def min_cost(i):
        #     if i < 2:
        #         return 0
        #
        #     return min(cost[i - 2] + min_cost(i - 2), cost[i - 1] + min_cost(i - 1))
        #
        # # we want the min cost to escape the array
        # return min_cost(n)

        # # Top down (memo) approach
        # n = len(cost)
        # memo = {0: 0, 1: 0}
        #
        # def min_cost(i):
        #     if i in memo:
        #         return memo[i]
        #     else:
        #         memo[i] = min(
        #             cost[i - 2] + min_cost(i - 2), cost[i - 1] + min_cost(i - 1)
        #         )
        #         return memo[i]
        #
        # return min_cost(n)

        # # Bottum up (tabulation) approach
        # n = len(cost)
        # dp = [0] * (n + 1)  # n+1 so that it exists the array
        #
        # for i in range(2, n + 1):
        #     dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
        #
        # return dp[n]

        # Bottom Up (tabulation) using constant space
        # current: 1 step back
        # prev: 2 steps back
        n = len(cost)

        # our base cases
        prev, curr = 0, 0

        for i in range(2, n + 1):
            prev, curr = curr, min(cost[i - 2] + prev, cost[i - 1] + curr)

        return curr
