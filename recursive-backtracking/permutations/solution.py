"""
Given an array nums of distint integers, return all the possible permutations (a rearrangement of
all the elements of an array). The order of the answer is not important.

Example 1:
nums = [1,2,3]
output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]


First number (3): 3 possiblities of starting point [1, 2, 3]
Second number (2): 2 different possibilites of second spot [1, 2]
Third number (1): 1 possiblitie of last spot [1]

3 * 2 * 1 = !3 = 6

                                           [ ]
           [1]                             [2]                           [3]                    # first nubmer (3 options)
    [1,2]      [1,3]                 [2,1]     [2,3]              [3,1]        [3,2]            # second number (2 options)
[1,2,3]         [1, 3, 2]       [2, 1, 3]       [2, 3, 1]       [3,1,2]         [3, 2, 1]       # third number (1 option)


Example 2:
nums = [0, 1]
output: [[0, 1], [1,0]]

        [ ]
[0, 1]        [1,0]

Solution:
We use a DFS to go through all of these combinations.
- at every step we iteratve over our number array
- this is true not only for the top but for every location, we use an if statment to check if the number has already been used.
- We only go down the paths that are needed to make a subset (ie numbers that have not been used yet)

- our fist sol[] array will look like: [1, 2, 3] (which is a DFS from the root)
    - first level: [1]
    - second level: [1, 2] (since 1 is used, we pick the leftmost of 2, 3)
    - third level: [1, 2, 3] (since 1 and 2 are used already we pick 3)

Time Complexity: O(n!)
Space: O(n) -> recursive callstack for height of tree which is n numbers
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        # res is our aray to return, sol is the current solution
        res, sol = [], []

        def backtrack():
            if len(sol) == n:
                # give res a copy of solution
                res.append(sol[:])
                return

            for num in nums:
                # only go down path if number is not in solution
                if num not in sol:
                    sol.append(num)
                    backtrack()
                    # this is the recursive backtracking part: undo the effect that we made
                    sol.pop()

        backtrack()
        return res
