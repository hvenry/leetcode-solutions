"""
Given two strings text1 and text2, return the legnth of their longest common subsequence. If there is no common
subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none)
deleted without changing the relative order of the remaining characters.

For example 'ace' is a subsequence of 'abcde'.

A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
text1 = "abcde", text2 = "ace"
returns 3

This is because the longest common subsequence is 'ace'.


Solution:

Idea: Base case (index out of bounds, return 0)
    - Place index on both of the strings and check if they are equal to each other.
    - When both the indexes match, we move them both up by one.
    - When they dont, we need to view all combinations of moving one index forward and leaving the other, and vice versa.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Top Down DP (memoization) using recursion
        # Time: O(m*n) -> we need to explore all paths of text1 (n), text2 (m)
        # Space: O(m*n) -> recursive callstack

        # m = len(text1)
        # n = len(text2)
        #
        # @cache
        # def longest(i, j):
        #     if i == m or j == n:
        #         return 0
        #     # use a character
        #     elif text1[i] == text2[j]:
        #         return 1 + longest(i + 1, j + 1)
        #     else:
        #         return max(longest(i, j + 1), longest(i + 1, j))
        #
        # return longest(0, 0)

        # bottom up (tabulation) approach
        # Time: O(m * n)
        # Space: O(m * n)

        """
        visualization example (start)
        m = gators
        n = agars
          a  g  a  r  s  -
        g 0  0  0  0  0  0
        a 0
        t 0
        o 0
        r 0
        s 0
        - 0

        visualization example (end)
        m = gators
        n = agars
          a  g  a  r  s  -
        g 0  0  0  0  0  0
        a 0  0  1  1  1  1
        t 0  1  1  1  1  1
        o 0  1  1  1  1  1
        r 0  1  1  2  2  2
        s 0  1  1  2  3  3
        - 0  1  1  2  3  4 <- we return this value dp[m][n]
        """
        m = len(text1)
        n = len(text2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # the [m][n] index will have the max value
        return dp[m][n]
