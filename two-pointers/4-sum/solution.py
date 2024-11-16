"""
Given an array nums of n integers, return an array of all the unique quaduplets
[nums[a], nums[b], nums[c], nums[d]] such that:
- 0 <= a, b, c, d, < n
- a,b,c,d are distinct
- nums[a] + nums[b] + nums[c] + nums[d] = target

Example 1:
nums = [1, 0, -1, 0, -2, 2]
target = 0

returns: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

Example 2:
nums = [2, 2, 2, 2, 2]
target = 8

returns: [[2, 2, 2, 2]]

Solution
- use 3-sum solution (sort array, find leftmost unique val, use two pointers from unqiue val to end of array, find two vals that sum to target using pointers)
- now add an extra embedded for loop for j that adds the 'fourth' value to get to our target, the code is extreamly similar to 3-sum.

To best visualize this, imagine i, j on the left side of the array, then left right between j and the end of the array.
- we then 'squeeze' a first time by moving j inwards squeezing the possible values of left and right,
- we then 'squeeze' eventually when there j has explored all of the subproblems from i to end, and now i gets moved in, squeezing j and left and right.
    - the first squeeze of i will go from i = 0  to i = 1 (assuming no duplicates), then this limits all the possible values j and left and right can take on

Complexity:
- Time O(n^3)
- Space O(1) -> assuming in place sorting
"""

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()

        for i in range(n - 3):
            # same number, we don't want to use it
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # this is the extension of 3 sum, we now have a j index too starting after index i
            for j in range(i + 1, n - 2):
                # we make j unique
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # we set left and right witihn j to n
                left, right = j + 1, n - 1

                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if sum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        # adjust left and right until the are unique
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    # adjust left and right to get closer to target
                    elif sum < target:
                        left += 1
                    else:
                        right -= 1

        return res
