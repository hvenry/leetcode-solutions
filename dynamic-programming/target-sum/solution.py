"""
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' or '-' before each
integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add '+' before 2 and '-' before 1 and concatenate them to
build teh expression "+2-1".

Return the number of different expressions that you can build, which evalutates to target.

Example:
nums = [1, 1, 1, 1, 1]
target = 3
returns: 5

- There are 5 ways to assign symbols to make the sum of nums be target 3.
    -1 + 1 + 1 + 1 + 1 = 3
    +1 - 1 + 1 + 1 + 1 = 3
    +1 + 1 - 1 + 1 + 1 = 3
    +1 + 1 + 1 - 1 + 1 = 3
    +1 + 1 + 1 + 1 - 1 = 3

Solution (backtrack + memo)
- Backtracking solution where terminating case is when i == n, and cur_sum == target

Optimized Approach:
- Use a bottom-up approach to calculate the number of target sums using previous answers

Example:
nums = [1, 1, 1, 1, 1]
target = 3

    -5      -4      -3      -2      -1      0       1       2       3       4       5
0                                           1
1                                   1               1
2                           1               2               1
3                   1               3               3               1
4           1               4               6               4               1
5   1               5               10              10              5 <- TARGET     1

- Using this table approach, we can figure out how many possible ways we can get to any value
  with 0 being the base case (1 way to get to 0)
- We then branch off to find how many ways there is to get to each value, by using the values of
  the previous rows.
    - To optimize even further, we can just use 2 rows at a time in memory, by construcing a dp
      array after each row called next_dp, and setting dp to next_dp when we find out values.

Complexity:
- Time: O(n * s) -> where s is the sum of numbers
- Space: O(s)
"""

from typing import List
from collections import defaultdict


# optimized approach only using 2 rows of memory
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for i in range(len(nums)):
            next_dp = defaultdict(int)
            for cur_sum, count in dp.items():
                next_dp[cur_sum + nums[i]] += count
                next_dp[cur_sum - nums[i]] += count
            dp = next_dp

        return dp[target]


# optimized approach
# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         dp = [defaultdict(int) for _ in range(len(nums) + 1)]
#         dp[0][0] = 1
#
#         for i in range(len(nums)):
#             for cur_sum, count in dp[i].items():
#                 dp[i + 1][cur_sum + nums[i]] += count
#                 dp[i + 1][cur_sum - nums[i]] += count
#
#         return dp[len(nums)][target]


# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         dp = {}
#
#         def backtrack(i, cur_sum):
#             if (i, cur_sum) in dp:
#                 return dp[(i, cur_sum)]
#             if i == len(nums):
#                 return 1 if cur_sum == target else 0
#
#             dp[(i, cur_sum)] = backtrack(i + 1, cur_sum + nums[i]) + backtrack(
#                 i + 1, cur_sum - nums[i]
#             )
#
#             return dp[(i, cur_sum)]
#
#         return backtrack(0, 0)
