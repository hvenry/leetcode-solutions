"""
You are given an integer array banned and two integers n and maxSum. You are choosing some number of integers
following the below rules:

- The chosen integers have to be in range [1, n].
- Each integer can be chosen at most once.
- The chosen integers should not be in the array banned.
- The sum of the chosen integers should not exceed maxSum.

Return the maximum number of integers you can choose following the mentioned rules.

Example:
banned = [1, 6, 5]
n = 5
maxSum = 6

returns: 2

- You can chose the integers 2, 4 which are in the range [1, 5], both do not appear in banned, and their sum
  does not exceed maxSum

Solution:
- Use a set to store banned numbers reduces from n^2 -> n complexity for O(1) lookup
- Iterate through range of 1 to n + 1
- If i is not in banned set and the current sum + i is <= maxSum, we can add 1 to our answer, and update our
  current sum.

Complexity:
- Time: O(n)
- Space: O(n) -> set
"""

from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ans = 0
        cur_sum = 0
        banned_set = set(banned)

        for i in range(1, n + 1):
            if i not in banned_set and cur_sum + i <= maxSum:
                ans += 1
                cur_sum += i

        return ans
