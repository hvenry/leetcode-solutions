from typing import List

"""
nums = [100, 4, 200, 1, 3, 2]
output: 4

because longest consecutive is [1, 2, 3, 4]

we could sort and this would be easy to solve by just
seeing what is n+1, but this would be O(nlogn) because
we need to sort.

each sequence has as start value, which has no left neighbor

we can find what the start values are by finding the number
that does not have a left neighbor

solution:
- iterate through original array
- use a set
- check if values have left neighbors
- if they dont, then they are the start of the sequence

Time O(n)
Space O(n)
"""


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
