"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its
neighbors.

Test case format:
For simplicty, each node's value is the same as the node's index (1-indexed).
For example, the first node with val == 1, the second node with val == 2,
and so on. The graph is represented in the test case using an adjaceny list.

An adjacency list is a collection of unordered lists used to represent a finite graph.
Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy
of the given node as a reference to the cloned graph.

Example:
adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
output: [[2, 4], [1, 3], [2, 4], [1, 3]]

Solution:
- use old_to_new to handle mappings of each original node to the clone node
- use a dfs and start by cloning the starting node and store it in old_to_new
- pop each node in the stack, and for each neighbor in current, clone it to old_to_new if it is
  not there already and push it to the stack
- then link the clone of the current node to the clone of the neighbor

old_to_new[node] should now contain a deep copy of the original node.

Complexity:
Time: O(n + e) -> visit each node, loop through each neighbor
Spae: O(n) -> worst case all nodes are in stack, hashmap stores e edges.
"""

from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        # since node is optional, it can be None
        if not node:
            return None

        # the beginning
        # map old nodes to new for a deep copy
        old_to_new = {node: Node(val=node.val)}

        # use an iterative stack
        stack = [node]

        while stack:
            current = stack.pop()

            # go through the neighbours of current
            for neighbor in current.neighbors:
                if neighbor not in old_to_new:
                    # clone neighbors of current
                    old_to_new[neighbor] = Node(val=neighbor.val)
                    # add neighbors to stack
                    stack.append(neighbor)

                # link the clone of current node to clone of neighbor
                old_to_new[current].neighbors.append(old_to_new[neighbor])

        return old_to_new[node]
