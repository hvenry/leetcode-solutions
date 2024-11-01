"""
There are a total of numCourses course you have to take, labeled from 0 to
numCourses - 1. You are given an array prerequesits where
prerequisites[i] = [a_i, b_i] indicates that you must take the course b_i
first if you want to take course a_i.

For example, the pair [0, 1] indicates that to take course 0 you have to first
take course 1.

Return the ordering fo courses you should take to finish all courses. If there are
many valid answers, return any of them. If it is impossible to finish all courses,
return an empty array.


Example:
numCourses = 4
prerequisites = [[1,0], [2,0], [3,1], [3,2]]
Output: [0, 2, 1, 3]

Graph:
1 --> 0
^     ^
|     |
3 --> 2

Ordering: [0, 1, 2, 3] or [0, 2, 1, 3]

Explanation: There are a total of 4 courses to take. To take corse 3 you should have
finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished
course 0.

So one correct course order is: [0, 1, 2, 3], another is [0, 2, 1, 3] (order of 1 and 2 dont matter)


Harder Exapmle:
N = 6
P = [[2, 0], [1, 0], [0, 3], [3, 4], [3, 5]]

2 --> 0 --> 3 --> 4
      ^     |
      |     v
      1     5

Solution:
- Do the whole 0 = UNSEEN, 1 = VISITING, 2 = VISITED
- Detect if there are cycles in the graph
  If there is a cycle, then there is a course that requires itself to already
  be done in order to take it, this means that there are no valid prerequisites to take it.
  Return an emptpy list here

Complexity:
- Time: O(n + e) -> we see all nodes and all edges (worse case DFS for neighbors in graph)
- Space: O(n + e) -> We are storing n verticies AND storing all edges in the graph
"""

from typing import List
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[a].append(b)

        UNSEEN = 0
        VISITING = 1
        VISITED = 2

        states = [UNSEEN] * numCourses

        # cycle detection
        def dfs(node):
            state = states[node]

            if state == VISITED:
                return True
            elif state == VISITING:
                return False

            states[node] = VISITING

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            states[node] = VISITED
            order.append(node)

            return True

        # try and take all courses
        for i in range(numCourses):
            if not dfs(i):
                return []

        return order
