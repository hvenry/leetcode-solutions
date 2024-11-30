"""
You are given a 0-indexed 2D integer array pairs where pairs[i] = [start_i, end_i]. An arrangement of pairs is
valid if for every index i where 1 <= i < pairs.length, we have end_i-1 == start_i.

Return any valid arrangement of pairs. (The inputs always allow for a valid arrangement of pairs).

Example 1:
pairs = [[5, 1], [4, 5], [11, 9], [9, 4]]
output = [[11,9], [9, 4], [4, 5], [5, 1]]

- This is a valid arrangment since end_i-1 always equals start_i
    end_0 = 9 == 9 = start_1
    end_1 = 4 == 4 = start_2
    end_2 = 5 == 5 = start_3

Context:
Eulerian Path -> A trail in a fininte graph that visits every edge exactly once (allowing for revisiting verticies).
Eulerian Circuit -> Uses every edge of a graph exactly once.

Solution:
Construct Graph
- Build an adjacency list (graph) to represent directed edges between nodes.
- Track out_degree (outgoing edges) and in_degree (incoming edges) for each node.

Find Start Node
- Find a node with out_degree - in_degree == 1, this will be the start of teh Eulerian path
- If no such node exists, any node from the pairs can be the start

Eulerian Path Traversal
- Perform a DFS to traverse the graph
- Add each node to the result list (res) after visiting all outgiong edges (post-order traversal)

Result Conversion
- Reverse the result list, since nodes are added in reverse order during traversal
- Return edges by pairing consecutive nodes from result.

Complexity:
- Time: O(V + E), where V is number of nodes, E is number of edges
- Space: O(V + E), storing recursive stack during DFS
"""

from typing import List


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        res = []
        graph = {}
        out_degree = {}
        in_degree = {}

        # Construct the graph with all nodes
        for start, end in pairs:
            if start not in graph:
                graph[start] = []
            if end not in graph:
                graph[end] = []
            graph[start].append(end)

            out_degree[start] = out_degree.get(start, 0) + 1
            in_degree[end] = in_degree.get(end, 0) + 1

        # Find the start node
        start_node = self.getStartNode(graph, out_degree, in_degree, pairs)

        # Perform Eulerian path traversal
        self.euler(graph, start_node, res)

        # Reverse the result since Eulerian paths are added in reverse order
        res.reverse()

        return [[res[i], res[i + 1]] for i in range(len(res) - 1)]

    def getStartNode(self, graph, out_degree, in_degree, pairs):
        # Find a node with out_degree - in_degree == 1 (start of Eulerian path)
        for node in graph:
            if out_degree.get(node, 0) - in_degree.get(node, 0) == 1:
                return node

        # If no such node, start with any node in the pairs
        return pairs[0][0]

    def euler(self, graph, u, res):
        # Special case of DFS, visited every edge exactly only once
        while graph[u]:
            v = graph[u].pop()
            self.euler(graph, v, res)
        res.append(u)
