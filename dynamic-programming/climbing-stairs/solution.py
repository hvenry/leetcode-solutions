"""
You are climbing a staircase. It takes n steps to reach the top.

Each tme you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example:
n = 2
output = 2

There are two ways to climb to the top.

Solution(s):
- we can reduce this to the fib problem

1. Recursive (naive approach): O(2^n)
2. Top Down (memo): O(n)
3. Bottom Up (tabulation): O(n)
4. Bottum up Constanct space: O(n) space: O(1)
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # # 1 .Recursive Approach
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        #
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)

        # # 2. Top down (memo):
        # memo = {1: 1, 2: 2}
        #
        # def f(n):
        #     if n in memo:
        #         return memo[n]
        #     else:
        #         memo[n] = f(n - 2) + f(n - 1)
        #         return memo[n]
        #
        # return f(n)

        # # 3. Bottom up (tabulation):
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        #
        # dp = [0] * n
        # dp[0] = 1
        # dp[1] = 2
        #
        # for i in range(2, n):
        #     dp[i] = dp[i-2] + dp[i-1]
        #
        # return dp[n-1]

        # 4. Bottom up constant space:
        if n == 1:
            return 1
        if n == 2:
            return 2

        prev = 1
        cur = 2

        for _ in range(2, n):
            prev, cur = cur, prev + cur

        return cur
