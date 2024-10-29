"""
Given an array of distint integers 'candidates' and a target integer 'target'
return a list of all unique combinations of 'candidates' where the chose numbers sum
to 'target'. You may return the combinations in any order.

The same number may be chosen from candiates an unlimited number of times. Two combinations
are unique if the frequency of at least one of the chosen numbers are different.

The test cases are generated such that the number of unqiue combinations that sum up to target
is less than 150 combinations for the given input.

Example 1:
candidates = [2, 3, 6, 7]
target = 7

Output: [[2, 2, 3], [7]]

Explanation:
2 and 3 are candiates and 2 + 2 + 3 = 7 (notice how numbers can be used twice)
7 is a candidate and 7 = 7.

Example 2:
candiates = [2, 3, 5], target = 8
Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]


Trial Solution:
for [2,3,5] and t = 8

Tree approach and recursive backtracking on each possible number:

                                             []
                [2]                         [3]                         [5]
    [2,2]       [2,3]       [2,5]
[2,2,2]..
[2,2,3]..

[2,2,5] - THIS IS A BAD APPROACH, WE WILL GET LOTS OF DUPLICATES

New Solution: Index approach

- left path: try the current number at index, and KEEP trying it.
- right path: do not use the number, and move on (this removed duplicates!)

                                [ ]                                 # (root node) left: index i=0 (pick 2) right: dont pick
                [2]                              [ ]                # (going from right node) left: index i=1 (pick 3) right: dont pick
        [2,2]           [2]                 [3]         [ ]         #
[2,2,3]      [2,2]X [2,3] [2]



X <- all the paths now with two 2s. The next path will be left: decide to pick 3, right: do not pick

Base cases:
- when we have a complete match to the target (sum of sol = target) we add to res
  - then we backtrack

- when the sol is greater than target, we do not add to res and then we backtrack

- when i is out of bounds (i is greater than length of candidates)

"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(candidates)

        def backtrack(i, cur_sum):
            # base case: when our solution is equal to the target
            if cur_sum == target:
                res.append(sol[:])
                return

            # base case: current sum is greater to target OR i == n (our of numbers to choose from)
            if cur_sum > target or i == n:
                return

            # path 1: do not use current number (cur sum does not change since no number used)
            backtrack(i + 1, cur_sum)

            # path 2: consider the next number (ie choose number at i)
            # This increases our current sum
            sol.append(candidates[i])
            cur_sum += candidates[i]

            backtrack(i, cur_sum)

            sol.pop()

        backtrack(0, 0)
        return res
