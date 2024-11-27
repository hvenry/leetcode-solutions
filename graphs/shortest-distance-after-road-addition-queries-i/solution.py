"""
You are given an integer n and a 2D integer array queries.

There ar n cities numbered from 0 to n - 1. Initially, there is a unidirectional road from city i to city i + 1
for all 0 <= i < n - 1.

queries[i] = [u_i, v_i] represents the addition of a new unidirectional road from city u_i to city v_i. After each
query, you need to fin the length of the shortest path from city 0 to city n - 1.

Return an array answer where for each i in range [0, queries.length - 1], answer[i] is the length of the shortest
path from city 0 to city n - 1 after processing the first i + 1 queries.

Example:
n = 5
queries = [[2, 4], [0, 2], [0, 4]]
returns: [3, 2, 1]

Explanation:
After query 1 (2 -> 4 added)
0 -> 1 -> 2 -> 3 -> 4
          2 ------> 4

- The shortest path from 0 to 4 is 3.

After query 2 (0 -> 2 added)
0 -> 1 -> 2 -> 3 -> 4
          2 ------> 4
0 ------> 2

- The shortest path from 0 to 4 is 2.

After query 3 (0 -> 4 added)
0 -> 1 -> 2 -> 3 -> 4
          2 ------> 4
0 ------> 2
0 ----------------> 4

- The shortest path from 0 to 4 is 1.

Therefore, we return [3, 2, 1]

Solution:
- Run a BFS every time we add a query to the adjaceny list, which returns the shortest lenght to n
    - make sure to rest the BFS and visited nodes every time
- Return the resulting list of shortest lenghts after using each query


Complexity:
- Time: O(q (n + m)) -> queries * the time complexity of a BFS (nodes + edges)
- Space: O(n + q)
"""

from collections import deque
from typing import List


class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        adj = [[i + 1] for i in range(n)]

        def shortest_path():
            q = deque()
            q.append((0, 0))

            # keep track of visited
            visited = set()
            visited.add((0, 0))

            while q:
                cur, length = q.popleft()

                if cur == n - 1:
                    return length

                for neighbor in adj[cur]:
                    if neighbor not in visited:
                        q.append((neighbor, length + 1))
                        visited.add(neighbor)

        res = []

        for source, destination in queries:
            adj[source].append(destination)
            res.append(shortest_path())

        return res
