"""
There exist two undirected trees with n and m nodes, numbered from 0 to n - 1 and from 0
to m - 1, respectively. You are given two 2D integer arrays edges1 and edges2 of lengths
n - 1 and m - 1, respectively, where edges1[i] = [a_i, b_i] indicates that there is an edge
between nodes a_i and b_i in the first tree and edges2[i] = [u_i, v_i] indicates that there
is an edge between nodes ui and vi in the second tree.

You must connect one node from the first tree with with another node from the second tree
with an edge.

Return the minimum possible diameter of the resulting tree.

The diameter of a tree is the length of the longest path between any two nodes in the
tree.

Example:
edges1 = [[0,1],[0,2],[0,3]]
edges2 = [[0,1]]
returns: 3
- A minimum diameter of 3 can be obtained by connecting node 0 from the first tree with
  any node from the second tree.


Solution:
- Find min diameter of each tree using a DFS and backtracking from each leaf node.
- Return the max of diameter 1 and 2, OR the distance of d1 / 2 + d2/ 2 + 1, as this is
  the distance connecting both trees.

Complexity:
- Time: O(n)
- Space: O(n)
"""

from typing import List
from collections import defaultdict
from math import ceil
import heapq


class Solution:
    def minimumDiameterAfterMerge(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> int:
        # function to build adjacency lists
        def build_adj(edges):
            adj = defaultdict(list)
            for n1, n2 in edges:
                adj[n1].append(n2)
                adj[n2].append(n1)

            return adj

        # DFS to find diameter of a tree, we calculate starting at a leaf node and go backwards
        def get_diameter(cur, parent, adj):
            max_diameter = 0
            max_child_paths = [0, 0]

            for nei in adj[cur]:
                if nei == parent:
                    continue

                nei_diameter, nei_max_leaf_path = get_diameter(nei, cur, adj)
                max_diameter = max(max_diameter, nei_diameter)

                heapq.heappush(max_child_paths, nei_max_leaf_path)
                heapq.heappop(max_child_paths)

            max_diameter = max(max_diameter, sum(max_child_paths))

            return [max_diameter, 1 + max(max_child_paths)]

        # adjacency lists for each tree
        adj1 = build_adj(edges1)
        adj2 = build_adj(edges2)

        # diameters of both trees
        d1, _ = get_diameter(0, -1, adj1)
        d2, _ = get_diameter(0, -1, adj2)

        # return the achievable diameter of either tree1, tree2, or the distance of them combined + 1
        return max(d1, d2, 1 + ceil(d1 / 2) + ceil(d2 / 2))
