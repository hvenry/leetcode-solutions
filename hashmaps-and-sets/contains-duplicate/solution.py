from typing import List 

'''
use a set to see if there is a duplicate
'''

class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    num_set = set()

    for i in nums:
      if i in num_set:
        return True
      num_set.add(i)
    return False

    # or 
    # for i in range(len(nums)):
    #   if nums[i] in num_set:
    #     return True
    #   num_set.add(nums[i])
    # return False
    
  # time: O(n)
  # space: O(n)
