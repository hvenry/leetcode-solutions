"""
Given two integers n and k, return all possible combinations of k numbers
chosen from range [1, n].


Example:
n = 4
k = 2

returns: [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]

                        [ ]                             # choose to pick 4
            []                          [4]             # choose to pick 3
    []              [3]          [4]          [4,3]     # choose to pick 2
       [2]     [3]     [3,2]   [4] [4,2]                # choose to pick 1
        [2,1]   [3,1]         [4,1]                     # choose to pick 0 (end)

[1] Base case: if we have picked 0 numbers, need 2 numbers, and there are 2 numbers that are left
we should not explore a branch that leads to 0 new numbers being added.

"""

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # n = len(nums)
        res, sol = [], []

        def backtrack(x):
            # base case: we want to stop when solution length is n
            if len(sol) == k:
                res.append(sol[:])
                return

            # the amount of numbers we have left (not to the left)
            left = x

            # the amonut we need is picked (items in solution) minus k (the length of which solutions should be)
            still_need = k - len(sol)

            # check if left is greater than the amount of numbers we still need (basecase [1])
            if left > still_need:
                backtrack(x - 1)

            # classic rescursive backtracking
            sol.append(x)
            backtrack(x - 1)
            sol.pop()

        backtrack(n)
        return res
