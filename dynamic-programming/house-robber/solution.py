"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and
it will automatically conatact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can
rob tonight without alerting the police.

Example 1:
nums = [1, 2, 3, 1]
output: 4

Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3), therefore
total amount is 1 + 3 = 4. All other combinations result in less money.

Solution:
Bottom up approach -> build an array that is the max amount of money to take at each step.

Example: [5, 3, 10, 10]

Go through the houses, and take the max of previous or current value.

[(5), 0, 0, 0] (take 5)

[5, (3 or 5), 0, 0] (take 5)

[5, 5, (10 + 5 or 5), 0] (take 15)

[5, 5, 15, (15 or 10 + 5)] (take 15)

[5, 5, 15, 15] -> we return 15 which is the max we can agin from robbing [5, 3, 10, 10] where robbing adjacent house sets off alarms.

Base cases:
    len = 1 -> take dp[0]
    len = 2 -> take max(dp[0], dp[1])

Recurrence relation: dp[i] = max(dp[i-1], dp[i-2] + nums[i])

OPTIMAL SOLUTION:
Constant space bottom up approach (since you only need 2 most recent houses (1 step back, 2 steps back))
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # # 1. recurrence relation: O(2^n)
        # n = len(nums)
        #
        # def helper(i):
        #     if n == 0:
        #         return nums[0]
        #     if n == 1:
        #         return max(nums[0], nums[1])
        #
        #     return max(helper(i - 1), helper(i - 2) + nums[i])
        #
        # return helper(n-1) # last index is n-1

        # # 2. TOP DOWN (memoized)
        # n = len(nums)
        #
        # if n == 1:
        #     return nums[0]
        # if n == 2:
        #     return max(nums[0], nums[1])
        #
        # # memoization
        # memo = {0: nums[0], 1: max(nums[0], nums[1])}
        #
        # def helper(i):
        #     if i in memo:
        #         return memo[i]
        #     else:
        #         memo[i] = max(helper(i - 1), nums[i] + helper(i - 2))
        #         return memo[i]
        #
        # return helper(n - 1)

        # # 3. bottom up (tabulation)
        # n = len(nums)
        # if n == 1:
        #     return nums[0]
        # if n == 2:
        #     return nums[1]
        #
        # dp = [0] * n
        #
        # # base cases
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])
        #
        # for i in range(2, n):
        #     dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        #
        # return dp[n - 1]

        # 4. bottom up (tabulation) constant space, time O(n)
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return nums[1]

        prev = nums[0]
        curr = max(nums[0], nums[1])

        for i in range(2, n):
            # prev 2 steps back, curr 1 step back
            prev, curr = curr, max(nums[i] + prev, curr)

        return curr
