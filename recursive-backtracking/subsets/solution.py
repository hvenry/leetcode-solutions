"""
Given an interger array nums of unique elements, return all possible subsets
(a subset of an array is a selcetion of elements including none of the array)

The solution must not contain any duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1, 2, 3]
Output: [[], [1], [2], [3], [1,3], [2,3], [1,2,3]]

2^3 (power set) 2*2*2 = 8 solutions

Left we dont pick, right we pick:
                        [ ]
            [ ]                         [1]
    [ ]           [2]           [1]         [1, 2]
[ ]    [3]      [2] [2, 3]   [1] [1,3]   [1,2] [1,2,3] = 8 solutions

Solution:
- Use a DFS to compute these values

go from first level [ ] all the way down to bottom left [ ] with a DFS ( recursive :D )

Use 2 Global Lists:
Sol = []
- partial solutions at any given part of the DFS
- we add to this when we have explored all the combinations of current sol
Res = []
- we will be appending current vals of solution (during the DFS) to get our final resulting list of lists


Complexity:
Time: O(2^n)
- this is beacuase there are 2^n nodes on the tree for a list of length n

Space: O(n)
- This is from recursion space O(n) -> recursive callstack
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        # recursive backtracking solutions tend to use res, sol
        # these are our global empty lists
        res, sol = [], []

        def backtrack(i):
            # index out of bounds (end of the array)
            if i == n:
                # append a copy [:] of sol to result
                res.append(sol[:])
                return
            # 2 paths
            # left: Don't pick nums[i] (this is the traversing down to the leftmost node)
            backtrack(i + 1)

            # right: Pick nums[i] (this is when we have hit that left boundary of DFS)
            sol.append(nums[i])
            backtrack(i + 1)

            # remove the selected number (right number) from the solutin, and continue DFS
            sol.pop()

        backtrack(0)
        return res
