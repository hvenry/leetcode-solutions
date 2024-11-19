"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

The algorithm must run in O(n) time.

Example 1:
nums = [100, 4, 200, 1, 3, 2]
returns: 4

The result is 4 because longest consecutive is [1, 2, 3, 4].


Naive Approach: Sorting
- we could sort and then iterate through sorted array keeping trak of a streak and max streak
- this has O(n log n) time complexity though because we need to sort

Optimal Solution: Hash Set
- Store values of nums into a set, then iterate through the values of the set
- keep track of a longest
- check if values have left neighbors
    - if they dont, then they are the start of the sequence, start length at 1
    - while the number + length is in the current set, keep increasing lenght by 1 until this is fales
    - set longest to max(length, longest)
- return longest

Complexity:
- Time: O(n) -> iterate through nums
- Space O(n) -> store nums
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        longest = 0

        for num in num_set:
            # check if current is start of a sequence
            if num - 1 not in num_set:
                length = 1

                # find the right most number in sequence
                while num + length in num_set:
                    length += 1

                longest = max(length, longest)

        return longest
