"""
There are a total of numCourses courses you have to take, labeled from 0 to
numCourses - 1. You are given an aray prerequesites where
prerequisites[i] = [a_i + b_i] indicates that you must take course b_i first
if you wan to take course a_i.

take course 1.
For example, the pair [0, 1], indicates that to take courses 0 you have to first

Return true if you can finish all courses. Otherwise, return false.

Example:
numCourses = 2
prerequisites = [[1, 0]]

output = true

Explanation:
There are a total of 2 courses to take. TO take course 1 you should have finished course
0. So it is possible.

Example 2:
numCourses = 2
prerequisites = [[1,0], [0,1]]
Output = false

Explanation:
There are a total of 2 courses to take. To take course 1 you should have finished course 0,
and to take course 0 you should also have finished course 1.

So it is impossible.


Solution: Detect if there is a cycle in the graph:

N = 3,
P = [[0, 1], [1, 2]]

Directed graph

    0--->1
        /
       v
       2

THIS IS SOLVABLE! (NO CYCLE IN GRAPH)

P = [[0, 1], [1, 2], [2, 0]]

    0 ---> 1
    ^      /
     \    /
      \  v
        2

THIS IS NOT SOLVABLE! (CYCLE IN GRAPH)


Nodes are in 1 of 3 states:
    Unvisisted = 0
    Visiting = 1
    Visited = 2

All nodes start at 0
Do a dfs, on the first node, set it to 1 as 'visiting'
- do a dfs to future nodes, switching them to 1 as 'visisted', until there are no more nodes after it
  when there are no nodes left, set the node to 2 to mark as 'visited'
- if you are able to visit all nodes, withiohut encountering a 'visiting' node (1) on any DFS path,
  then there is no cylces and you can return true.
- if you find a 'visiting' node in a dfs path, then return False since there is a cycle


Complexity;
Time: O(N + E) -> go through at least all edges
Space: O(N + E) -> dfs callstack is O(N), O(E) is the graph edges we are storing
"""

from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequesites: List[List[int]]) -> bool:
        # build the graph
        graph = defaultdict(list)

        for a, b in prerequesites:
            # singly list graph
            graph[a].append(b)

        # constants
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        # track seen or not
        states = [UNVISITED] * numCourses

        def dfs(node):
            state = states[node]

            # check to see if current node leads to a cycle or not
            if state == VISITED:
                return True
            elif state == VISITING:
                return False

            # set the node we are currently at to visiting
            states[node] = VISITING

            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False

            states[node] = VISITED
            return True

        for i in range(numCourses):
            # dfs returned False, meaning a cylce was detected
            if not dfs(i):
                return False

        # If dfs did not return False at any given node, then there are no cylces
        return True
