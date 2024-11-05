"""
The Fibonacci numbers, commonly denoted F(n) from a sequence, called the Fibonacci sequence, such that each
number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n-1) + F(n-2), for n > 1

Given n, calculate F(n).

Example:
n = 4
returns 3 -> F(4) = F(3) + F(2) = 2 + 1 = 3


Recursive Approach: O(2^n), not
if n == 0:
    return 0
if n == 1:
    return 1

return self.fib(n - 2) + self.fib(n - 1)


Top-Down Memoization Approach:
                F(6)
        F(5)                F(4)
    F(4)    F(3)        F(3)    F(2)

Notice how F(4) is showing up multiple times, how do we optimize this? (overlapping subproblems)

At every step (n+1), we are DOUBLING, this means our code is going to be O(2^n) how do we optimize this?

Top-down (memoization) approach:
- idea: if we have computed a function call before, do not recompute it.
- we can use a hashmap (more generally, a cache), this is the term 'memo'

Using this approach, we only need to go the depth of the tree!

Complexity:
    Time: O(n)
    Space: O(n)


Bottom-up Tabulation Approach:

This approach eliminates recursion. The tabulation term comes from the array.

[0, 1, 1, 2, 3, 5, 8, 13]

Approach:
- createa an array and fill it with 0's (avoids using append)

Complexity
    Time: O(n)
    Space: O(n)
"""


class Solution:
    def fib(self, n: int) -> int:
        # # top down approach
        # memo = {0: 0, 1: 1}
        #
        # def f(x):
        #     if x in memo:
        #         return memo[x]
        #     else:
        #         memo[x] = f(x - 1) + f(x - 2)
        #         return memo[x]
        #
        # return f(n)

        if n == 0:
            return 0
        if n == 1:
            return 1

        # # bottom up approach
        # dp = [0] * (n + 1)
        #
        # dp[0] = 0
        # dp[1] = 1
        #
        # for i in range(2, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        #
        # return dp[n]

        # final optimization (turn into constant space)
        prev = 0
        cur = 1

        for _ in range(2, n + 1):
            prev, cur = cur, prev + cur

        return cur

        # # golden ratio approach (1 off approach)
        # golden_ratio = (1 + (5**0.5)) / 2
        # return int(round((golden_ratio**n) / (5**0.5)))
