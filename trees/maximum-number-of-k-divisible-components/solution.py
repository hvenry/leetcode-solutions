"""
There is an undirectre tree with n nodes labeled from 0 to n - 1. You are given the
integer n and a 2D integer array edges of length n -1, where edges[i] = [a_i, b_i]
indicates an edge between nodes a_i and b_i in the tree.

You are also given a 0-indexed integer array values of length n, where values[i] is
the value associated with the ith node, and an integer k.

A valid split of the tree is obtained by removing any set of edges, possibly empty,
from the tree such that the resulting components all have values that are divisible
by k, where the value of a connected component is the sum of the values of its nodes.

Return the maximum number of components in any valid split.

Example:
n = 7
edges = [[0,1], [0,2], [1,3], [1,4], [2,5], [2,6]]
values  = [3, 0, 6, 1, 5, 2, 1]
k = 3
returns: 6

Explanation:
node index:           vals:
        0                       3
    2       1       ->      0       6
   3 4     5 6             1 5     5  1

groupings:
1: node [0],        component sum = 3                3 % k = 0
2: node [2, 5, 6],  component sum = 6 + 1 + 2 = 9    9 % k = 0
3: node [1, 3, 4],  component sum = 0 + 5 + 1 = 6    6 % k = 0

Solution:
- This seems like a tricky problem on first glance, but with a DFS we can find
  subtrees that have a sume where %k = 0.
- We start at the root, and try to find valid subtrees that satisfy this condition
  until we reach leaf nodes, leading to a O(n) runtime and O(n) space (recursive callstack)


Complexity:
- Time: O(n)
- Space: O(n)
"""

from typing import List
from collections import defaultdict


class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int
    ) -> int:
        def dfs(node: int, parent: int) -> int:
            total_sum = values[node]

            for neighbor in graph[node]:
                if neighbor != parent:
                    child_sum = dfs(neighbor, node)
                    if child_sum % k == 0:
                        nonlocal res
                        res += 1
                    else:
                        total_sum += child_sum

            return total_sum

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        res = 0
        total_sum = dfs(0, -1)

        if total_sum % k == 0:
            res += 1

        return res
