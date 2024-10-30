"""
There is a bi-directional graph with n vertices, where each vertex is labeled
from 0 to n-1 (inclusive). The edges in the graph are represented as a 2D integer
array edges, between vertex u_i and vertex v_i. Every vertex pair is connected by
at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to
vertex destination.

Given edges and the integers n, source, and destination, return true if there is a
valid path from source to destination, or false otherwise.

Constraints:
- there are no duplicate edges
- there are no self edges

Example 1:

Input:
n=3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2

0---1
\   /
  2

Output: true
Explanation: There are two paths from vertex 0 to vertex 2.
0 -> 1 -> 2
0 -> 2

DFS Solution:
- do a DFS, keeping trakc of nodes we have already visited in a set
- return True if destination is added to set, false otherwise

BFS Solution:
- do a BFS, do the saem thing and keep track of nodes to see if we have visited it yet
- return True if destination is added to set, false otherwise

Complexity:
- Time: O(N+E) both of these solutions take up O(N+E) time (we go to every node, and see every edge in worse case)

"""

from typing import List
from collections import defaultdict
# # needed for BFS solution
# from collections import deque


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        # DFS with recursion
        # base case
        if source == destination:
            return True

        # Adjaceny list using dictionary
        # defaultdict never raises a KeyError (it provides a default value for the key that does not exist)
        graph = defaultdict(list)

        # bi-directional graph creation
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # make sure we do not repeatedly visit nodes (add souce to seen and any newly visited nodes)
        seen = set()
        seen.add(source)

        # dfs takes a node (i)
        def dfs(i):
            # base case
            if i == destination:
                return True

            # look through each neighbor at graph index i
            for j in graph[i]:
                if j not in seen:
                    seen.add(j)
                    if dfs(j):
                        return True

            return False

        return dfs(source)

        # dfs returns true if destination is found from source, false otherwise
        # return dfs(source)

        # # DFS wit stack (iterative)
        # # LIFO (last element in the stack gets taken out first)
        # # start with a stack and first node being source
        # stack = [source]
        #
        # while stack:
        #     i = stack.pop()
        #     if i == destination:
        #         return True
        #     for j in graph[i]:
        #         if j not in seen:
        #             seen.add(j)
        #             # appending to right side and popping from right side will cause a dfs
        #             stack.append(j)
        #
        # # not found
        # return False

        # # BFS with Deque
        # # FIFO (first element in the queue is the first out)
        # q = deque()
        # q.append(source)
        #
        # while q:
        #     # take away from the left, add to the right
        #     i = q.popleft()
        #     if i == destination:
        #         return True
        #
        #     for j in graph[i]:
        #         if j not in seen:
        #             seen.add(j)
        #             # add to the right
        #             q.append(j)
        #
        # # not found
        # return False
