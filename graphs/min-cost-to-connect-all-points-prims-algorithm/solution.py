"""
You are given an array points representing integer coordinates of some points
on a 2D-plane, where pints[i] = [x_i, y_i].

The cost of connecting two pints [x_i, y_i] and [x_j, x_j] is the manhanttan
distance between them: |x_i - x_j| + |y_i - y_j| where |val| denotes the
absolute value of val.

Return the minimum cost to make all pints connected. All points are connected
if there is exactly one simple path between any two points.

Example:
points = [[0, 0], [2, 2,], [3, 10], [5, 2], [7, 0]]
output = 20

We can connect the points as shown to get a minimum cost of 20.

[0, 0] -> [2, 2] (cost += 4)

[2, 2]
    -> [5, 2] |2 - 5| + |2 - 2| = 3 (cost += 3)
    -> [3, 10] (cost += 9)

[5, 2] -> [7, 0] (cost +=4)

All the points are connected with a min cost of 4 + 3 + 9 + 4 = 20.


Solution: Create a Minimum Spanning Tree (MST)
- If there are n points, the MST will have n - 1 edges.
- an nth edge will create a cycle


Two approaches to solve this: Prim's, Kruskall's

How to solve with Prim's
- Use a Seen set (to track nodes we have seen) and a Min Heap (organized by distances)
    - start at first node (0), which we are 0 distance away from, so (0, 0) is added to the heap (node index, distance)
    - while we have a heap, pop pop an element from it
    - go through every available neighbor of the current node (point), and calculate the distance it takes to get to it it's neighbors, storing these values in the heap
    - after calculating neighbors, we then pop the next node from the heap, which is the shortest distance from the previous point
    - if it's not in seen, calculate neighbors and add their (distance, index) to heap
    - keep going until you have seen all nodes in the graph, then the MST has been formed


Complexity:
- Time: O(n^2 log(n)) -> n^2 edges for n points, log(n^2) (edges we need to push to the heap)
  can be rewritten as O(E log(E)) where E is edges.
- Space: O(n^2) -> n^2 edges stored in the heap
"""

from typing import List
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        total_cost = 0
        seen = set()

        # add first node and it's distance from itself of 0
        min_heap = [(0, 0)]

        while len(seen) < n:
            # get first node from heapq
            distance, i = heapq.heappop(min_heap)

            # if we have already seen i, keep popping
            if i in seen:
                continue

            # if we have not seen the node, add it to seen
            seen.add(i)

            # increment total cost
            total_cost += distance

            # get the x and y coordinates of the point we are currently visiting
            x_i, y_i = points[i]

            # go through all possible neighbors of point
            for neighbor in range(n):
                # if a neighbor is not in seen, we want to calculate the distance to it and add to our heap
                if neighbor not in seen:
                    x_j, y_j = points[neighbor]
                    neighbor_distance = abs(x_i - x_j) + abs(y_i - y_j)
                    heapq.heappush(min_heap, (neighbor_distance, neighbor))

        # return the total cost
        return total_cost
