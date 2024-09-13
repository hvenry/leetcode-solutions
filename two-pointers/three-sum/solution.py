from typing import List

"""
given an integer array nums, return the triplets [nums[i], nums[j], nums[k]] such that

i != j
i != k
j != k
nums[i] + nums[j] + nums[k] = 0

example

nums = [-1, 0, 1, 2, -1, 4]
result: [[-1, -1, 2], [-1, 0, 1]]

why:
nums[0], + nums[1] + nums[2] = (-1) + 0 + 1 = 0  
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0      # not distinct from above
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0

the distinct triplets are: [-1, 0, 1], and [-1, -1, 2]


** similar to two-sum II (this uses the two-pointers technique) **


first approach: use a triple for loop. (this is not good, we will find lots of duplicates)
- go to each index "a' and look for a "b" + "c" that will sum to a,

Time: O(n^3)

better approach: sort the input array
- if left neighbor of next number is the same, skip (skips the duplicate)
- go next, and then find the 2 numbers that sum to current (use two pointers technique learned from two sum II)
    - shift left pointer in if the current sum is less than target, shift right pointer in if the current sum is larger than target
    - also skip over previously 

    
    Time Complexity
sorting: O(n log n)
two pointers for n numbers: O(n^2)
total: O(nlogn) + O(n^2) = O(n^2)

    Space Complexity
O(1) -> sometimes sorting can take O(n) space



"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # same value as before, skip
            if i > 0 and a == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                threeSum = a + nums[left] + nums[right]
                # move pointers inwards based on if we are above or below the target value
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    # only move left pointer, conditions above will update the right pointer (shift left until it is unique)
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return res
