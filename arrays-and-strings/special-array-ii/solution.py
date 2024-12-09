"""
An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integer nums and a 2D integer matrix queries, where for queries[i] = [from_i, to_i] your
task is to check if the subarray nums[from_i .. to_i] is special or not.

Return an array of booleans answer such that answer[i] is true if nums[from_i .. to_i] is special.

Example:
nums = [3, 4, 1, 2, 6]
queries = [[0, 4]]

returns: [false]
- The subarray is [3, 4, 1, 2, 6], 2 and 6 are both even and are adjacent to each other, making it not special.

Intuition:
- We can iterate through each query, and validate the queries start to end to see if any there are any 2 numbers
  where both of their %2 are equal. Append False to the array and exit early if this is the case, True otherwise.

Why this is suboptimal:
- There are multiple subproblems that overlap, one query could be [0, 2] and another query could be [0, 4], it does
  not make sense to recompute index 0, 1, 2 more than 1 time.
- To solve this, we can precompute the parity diff of every 2 numbers, and then we can resolve each query in O(1) time.

Solution:
- Precompute prefix array of the parity for each pair, then process each query to see if the range is special using prefix.

Visualization:
nums = [4, 3, 1, 6], queries = [[0, 2], [2, 3], [0, 3]]

start with array prefix:
prefix = [0, 0, 0, 0]

iterate over nums to calculate prefix:
prefix = [0, 0, 1, 1]
          <  >  <  > - valid ranges, if we compare a query that s=0, e=1 we know there are 2 numbers that violate the parity

process queries:
query [0, 2]:
prefix[2] - prefix[0] = 1 - 0 = 1
- since the result is not 0, there is at least one same-parity consecutive pair in the range [0, 2], append False

query [2, 3]
prefix[3] - prefix[2] = 1 - 1 = 0
- no same-parity consecutive pairs in range [2, 3], append True

query [0, 3]
prefix[3] - prefix[0] = 1 - 0 = 1
- at least one same-parity consecutive pair in range [0, 3], append False


Complexity:
- Time: O(n + q)
- Space: O(n)
"""

from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        m = len(queries)
        res = [False] * m
        n = len(nums)
        prefix = [0] * n

        # calculate prefix array
        for i in range(1, n):
            # check if same parity or not
            if nums[i] % 2 == nums[i - 1] % 2:
                # increment count of the same parity pairs
                prefix[i] = 1 + prefix[i - 1]
            else:
                # do not increment
                prefix[i] = prefix[i - 1]

        # process each query
        for i in range(m):
            # start and end indices of the query range
            s, e = queries[i]
            # check if no consecutive same-parity elements exist in the range, if there is a change we know it is not special
            res[i] = prefix[e] - prefix[s] == 0

        return res

        # # Naive approach
        # res = []
        #
        # for query in queries:
        #     start, end = query
        #     is_special = True
        #
        #     for i in range(start, end):
        #         if i + 1 >= len(nums):
        #             is_special = False
        #             break
        #
        #     if nums[i] % 2 == nums[i + 1] % 2:
        #         is_special = False
        #         break
        #
        #     res.append(is_special)
        #
        # return res
