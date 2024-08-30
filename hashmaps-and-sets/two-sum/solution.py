from typing import List

'''
nums = [2, 7, 11, 15]
target = 9

expected: [0, 1]

how to solve with hashmap:

- go through every num in nums
      print(hashmap)
- check if matching (which is target - num) is in our hashmap
- if it is in hashmap, return array [ hashmap[matching] , num ]

example:

hashmap = {}

iteration 1:
num = 2
matching = 9 - 2 = 7
hashmap = { 2 : 0 }

iteration 2:
num = 7
matching = 9 - 7 = 2

matching IS in hashmap ( { 2 : 0 } )
we now return [ 0 (comes from hashmap[matching] or hashmap[2]), 1 (comes from i)]

res = [0, 1]
'''

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashmap = {}

    for i in range(len(nums)):
      matching = target - nums[i]
      # O(1) lookup time in hashmap
      if matching in hashmap:
        return [hashmap [matching], i]
      hashmap[nums[i]] = i
    return []
  
  # time: O(n)
  # space: O(n)
