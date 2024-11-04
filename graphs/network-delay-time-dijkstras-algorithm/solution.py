"""
You are given a network of n nodes, labeled from 1 to n. You are also given
times, a list of travel times as directed edges times[i] = (u_i, v_i, w_i),
where u_i is the source node, v_i is the target node, and w_i is the time it
takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes
for all the n nodes to recieve the signal. If it is impossible for all the n
nodes to recieve the signal, return -1.

Example:
times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]], n = 4, k = 2

  (1)   (1)   (1)
1 <-- 2 --> 3 --> 4

output = 2

Signal coming from 2, how long does it take to get to all nodes?
    it takes 1 to go from 2->1
    it takes 1 + 1 to go from 2->3->4.

All nodes are visisted now.

Solution: Use Dijkstra's Algorithm
We will need:
- hashmap min_times, that maps keys with the total distance it takes to get to the node
- min heap min_heap, that organizes the total distance it takes to get to a node from the source, and the node to get there

While we have a min_heap that is initialzied at our source and the distance to get there which is 0
- append the min_time to get to the source (0)
- check the neighbors of the source node, and append (distance, node) to the min_heap.
- the smaller distance will be on the top, so when we pop this we will be at the closest node from the node before it
- if we have not been to the node before, then we add it to the min_time to get there!
    - This never gets updated again! This is the smallest distance, based off of the min_heap.

- we then carry on, using the TOTAL distance to see how far neighboring nodes are, and add this to the stack
    - By popping from the min heap after this, we are essentially getting the MIN DISTANCE to a given node from our SOURCE.
    - we want to RETURN THE MAX of these distances, to determine what the MAX TIME IS.

Complexity:
Time: O((V + E) log(V))
Space: O(V + E)
"""

from typing import List
from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # adjaceny list
        graph = defaultdict(list)

        # create graph mappings (1 direction from u to v)
        for u, v, time in times:
            graph[u].append((v, time))

        # store our min_times to travel to each node
        min_times = {}

        # distance from source (k) which is 0, our source node (k)
        min_heap = [(0, k)]

        while min_heap:
            # get the min distance value from the heap
            time_k_to_i, i = heapq.heappop(min_heap)

            # if we have already seen the node, skip
            if i in min_times:
                continue

            # if we have not seen this node yet, it is the min time to get to it (since it is popped from the min heap)
            min_times[i] = time_k_to_i

            # check all the neighbors of the current node i
            for neighbor, neighbor_time in graph[i]:
                if neighbor not in min_times:
                    # if the min time for this node has not been found, we add the path distance (TOTAL DISTANCE) and neighbor node to heap
                    heapq.heappush(min_heap, (time_k_to_i + neighbor_time, neighbor))

        # if our min_times is the same as number of nodes (we could get to all nodes in the graph)
        if len(min_times) == n:
            return max(min_times.values())
        else:
            return -1
