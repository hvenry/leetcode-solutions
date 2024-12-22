"""
You are given a 0-indexed array heights of positive integers, where heights[i] represents the
height of the ith building.

If a person is in a building i, they can move to any other building j if and only if i < j and
heights[i] < heights[j].

You are also given another array queries where queries[i] = [a_i, b_i]. On the ith query, Alice
is in building a_i, while Bob is in building b_i.

Return an array ans where ans[i] is the index of the leftmost building where Alice and Bob can
meet on the ith query. If Alice and Bob cannot move to a common building on query i, set
ans[i] to -1.

Example:
heights = [6,4,8,5,2,7]
queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]
returns: [2, 5, -1, 5, 2]

- Query 1 can be answered by having them both move to building 2, since 8 is greater than 4, 6.
    - (Alice is at building 0 (height of 6), Bob is at building 1 (height of 4), Alice cannot
      simply move to Bobs building since 6 is larger than 4, they must both meet at building 2
      (value 8), becuase they can only go right to a building with a larger height.

Solution (Brute Force):
- We know that all we are searching for is a the leftmost valid building for each pair of values.
- This can be found by for each query, use left and right boundaries to check either:
    - If they equal each other (left==right), then the answer is the current building.
    - Else, we check all the possible values from right to heights, and when the value is found
      that is larger than height, we have located our solution.

Solution (Optimal):
- Group the queries by the right index, so each index has a required height.
- For queries where heights[right] > heights[left], resolve them, right is already valid.
- Use a min-heap to manage query conditions, the use of this allows for quick access to the smallest
  required_height, making it easy to check if the current building satisfies a query.
- Iterate through each height, and:
    - Push query conditions for the current index to the heap
    - Check the top of the heap, if the current building exceeds the required_heaight of a query,
      resolve the query and remove it from the heap.
"""

import heapq
from typing import List
from collections import defaultdict


# Optimal
class Solution:
    def leftmostBuildingQueries(
        self, heights: List[int], queries: List[List[int]]
    ) -> List[int]:
        res = [-1] * len(queries)

        # for each right value, we map a (required_height, query_index)
        groups = defaultdict(list)

        for index, query in enumerate(queries):
            # query may not be in order so we sort
            left, right = sorted(query)

            # query can be answered if right is larger than left
            if left == right or heights[right] > heights[left]:
                res[index] = right
            # if no immediate answer, we take max height at both indices and append to groups
            # this is used to validate query through a range
            else:
                height = max(heights[left], heights[right])
                groups[right].append((height, index))

        min_heap = []

        for index, height in enumerate(heights):
            # push all the query values to the heap
            for query_height, query_index in groups[index]:
                heapq.heappush(min_heap, (query_height, query_index))

            # check current height can be answered with heap at the top of the min heap
            while min_heap and height > min_heap[0][0]:
                query_height, query_index = heapq.heappop(min_heap)
                res[query_index] = index

        return res


# # Brute Force
# class Solution:
#     def lestmostBuildingQueries(self, heights: List[int], queries: List[List[int]]):
#         res = [-1] * len(queries)
#
#         for index, query in enumerate(queries):
#             left, right = sorted(query)
#
#             if left == right or heights[right] > heights[left]:
#                 res[index] = right
#                 continue
#
#             for j in range(right + 1, len(heights)):
#                 if heights[j] > max(heights[left], heights[right]):
#                     res[index] = j
#                     break
#
#         return res
