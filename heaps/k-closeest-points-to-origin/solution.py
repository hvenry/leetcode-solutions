"""
Given an arary of ponts where points[i] = [x_i, y_i] represents a point on the
X-Y plane and an integer k, returns the k closest points to the origin (0, 0).

The diestance between two points on the X-Y plane is the Euclidean diestance
    (ie sqrt( (x_1 - x_2)^2 + (y_1 - y_2)^2 )

You may return the answer in any order. The answer is guaranteed to be unique
(except for the order that it is in).

Example:
points = [[1, 3], [-2, 2]], k=1
output: [[-2, 2]]

The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).

Since sqrt(8) < sqrt(10) the points (-2, 2) is closer to the origin.

We only want the closest k=1 points from the origin, so the answer is just [[-2, 2]].


Example:
[[3,3], [2,2], [4,4], [1,1]]
d(0) = 18
d(1) = 8
d(2) = 32
d(3) = 2


Solution Approach:

Optimizations to formula:
- we can simplify this formula:
d = sqrt( (x_1 - x_2)^2 + (y_1 - y_2)^2 )
d = sqrt( (x_1)^2 + (y_1)^2 ) # x_2, y_2 is always the origin, meaning they are always both 0
d = (x_1)^2 + (y_1)^2 # you don't need square root since it is changing our result by a constant factor

- use a minheap for k log n time
- this is faster than n log n time (just sorting and returning k values from 0), becasue we can make an assumption
  that k is much less than n, ie it is unrealistic that k will always be the size of our inputs.

- we need to compute the distance of all points

Maxheap approach:
- never store more than k elements in the heap
- we always pop off the top element to make sure that we dont go over k elements (this is done with a pushpop)

O(n * log k)
-> we need to traverse the whole array (n)
-> we need to insert into heap that is at most k length (log k)
"""

from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return x**2 + y**2

        heap = []
        for x, y in points:
            d = dist(x, y)
            if len(heap) < k:
                # for max heap functionality, we need to negate the distance
                heapq.heappush(heap, (-d, x, y))
            else:
                heapq.heappushpop(heap, (-d, x, y))

        return [(x, y) for d, x, y in heap]
