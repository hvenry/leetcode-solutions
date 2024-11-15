"""
Given an integer array nums, return the triplets [nums[i], nums[j], nums[k]] such that

i != j  |
i != k  |- may not contain duplicate triplets
j != k  |

and nums[i] + nums[j] + nums[k] = 0.

Example 1:
nums = [-1, 0, 1, 2, -1, 4]
returns: [[-1, -1, 2], [-1, 0, 1]]

nums[0] + nums[1] + nums[2] = (-1) + 0 +   1  = 0
nums[1] + nums[2] + nums[4] =   0  + 1 + (-1) = 0   <- not distinct from above
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0

the distinct triplets are: [-1, 0, 1], and [-1, -1, 2]

Naive Approach:
- Use a triple for loop, go to each index "a' and look for a "b" + "c" that will sum to a.
- this will give us a lot of duplicates and a time complexity of O(n^3)

Solution:
- sort the input array
- if left neighbor of next number is the same, skip (skips the duplicate)
- iterate through the remainder of the array and find the 2 numbers that sum to current (similar to two sum ii)
    - shift left pointer in if the current sum is less than target, shift right pointer in if the current sum is larger than target
    - also skip over previously used numbers
    - whenever we the difference of the 2 values is 0, we store it as an answer
    - we keep doing thins until left and right intersect, storing any answers found along the way

Visualization:
    [-3, -3, -2, -1, 0, 1, 2, 2, 3]
      i   <---------------------->
         left and right search this

    [-3, -3, -2, -1, 0, 1, 2, 2, 3]
      i              l           r    -> this is a valid solution [-3, 0, 3]


    [-3, -3, -2, -1, 0, 1, 2, 2, 3]
      i                 l     r       -> this is another valid solution [-3, 1, 2]

- Our answer so far (after just checking ith number) is [[-3, 0, 3], [-3, 1, 2]]

- We then continue at the next unique index starting like this:
    [-3, -3, -2, -1, 0, 1, 2, 2, 3]
              i   l              r


Complexity:
- Time: O(n^2)
    - sorting: O(n log n)
    - two pointers for n numbers: O(n^2)
- Space: O(1) (assuming sorting in place)
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if nums[i] > 0:
                break
            # skip duplicates
            elif i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left, right = left + 1, right - 1

                    # make suer neither are on the same value
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1

        return res
