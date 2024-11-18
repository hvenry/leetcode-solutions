"""
Given an array of integers nums and an integer target, return indices of the two numbers such
that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element
twice.

You can return the answer in any order.

nums = [2, 7, 11, 15]
target = 9

expected: [0, 1]

Solution:
- to get better than O(n^2) time, use a hashmap
- go through every num in nums
- check if matching (which is target - num) is in our hashmap
- if it is in hashmap, return array [ hashmap[matching] , num ]

Visualization:
hashmap = {}

i = 0:
num = 2
matching = 9 - 2 = 7
hashmap = { 2 : 0 }

iteration 1:
num = 7
matching = 9 - 7 = 2
matching IS in hashmap ( { 2 : 0 } )

we now return [ 0 (comes from hashmap[matching] or hashmap[2]), 1 (comes from i)]
res = [0, 1]

Complexity:
- Time: O(n)
- Space: O(n)
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            matching = target - nums[i]
            # O(1) lookup time in hashmap
            if matching in hashmap:
                return [hashmap[matching], i]
            hashmap[nums[i]] = i
        return []
