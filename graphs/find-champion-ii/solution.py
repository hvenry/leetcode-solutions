"""
There are n teams numbered from 0 to n - 1 in a tournament; each team is also a node in DAG (directed acyclic graph)

DAG: Nodes are directionally related to each other and don't form a cylce.

You are given an integer n and a 0-indexed 2D integer array edges of length m representing the DAG, where
edges[i] = [u_i, v_i] indicates that there is a directed edge from team u_i to team v_i in the graph.

A directed edge from a to b in the graph means that  team a is stronger than team b, and team b is weaker than
team a.

Return the team that will be the champion of the tournament if there is a unique champion, otherwise, return -1.

Example 1:
n = 3
edges = [[0, 1], [1, 2]]
returns: 0

- Team 1 is weaker than team 0. Team 2 is weaker than team 1. The champion is team 0!

Example 2:
n = 4
edges = [[0, 2], [1, 3], [1, 2]]
returns: -1

- Team 2 is weaker than team 0 and team 1. Team 3 is weaker tahn team 1. BUT team 1 and team 0 are not weaker
  than any other teams, so there is not a unique champion.


Solution:
- Create an adjacency list, count the amount of incomming edges to a node
- Find all nodes that have a count of 0 incomming edges (they are a champion)
- If the length of champions is > 1, return -1, else return the champion's value (same as index).

Complexity:
- Time: O(n)
- Space: O(n)
"""

from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        incoming = [0] * n

        # Count the amount of edges going to a destination
        for _, destination in edges:
            incoming[destination] += 1

        champions = []

        # If there are no incoming edges to i (count is 0), it is a champion
        for i, incoming_count in enumerate(incoming):
            if not incoming_count:
                champions.append(i)

        # Return -1 if there is not 1 champion
        if len(champions) > 1:
            return -1

        # Return the value of the unique champion
        return champions[0]
