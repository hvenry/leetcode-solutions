import unittest
from solution import Node, Solution


class TestCloneGraph(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def build_graph(self, adjList):
        if not adjList:
            return None

        nodes = [Node(i + 1) for i in range(len(adjList))]
        for i, neighbors in enumerate(adjList):
            nodes[i].neighbors = [nodes[j - 1] for j in neighbors]
        return nodes[0]

    def graph_to_adjList(self, node):
        if not node:
            return []

        adjList = {}
        stack = [node]
        visited = set()

        while stack:
            current = stack.pop()
            if current.val not in visited:
                visited.add(current.val)
                adjList[current.val] = [neighbor.val for neighbor in current.neighbors]
                for neighbor in current.neighbors:
                    if neighbor.val not in visited:
                        stack.append(neighbor)

        return [adjList[i] for i in range(1, len(adjList) + 1)]

    def test_clone_graph(self):
        adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
        original = self.build_graph(adjList)
        cloned = self.solution.cloneGraph(original)
        self.assertEqual(self.graph_to_adjList(cloned), adjList)

    def test_empty_graph(self):
        adjList = []
        original = self.build_graph(adjList)
        cloned = self.solution.cloneGraph(original)
        self.assertEqual(self.graph_to_adjList(cloned), adjList)

    def test_single_node_graph(self):
        adjList = [[]]
        original = self.build_graph(adjList)
        cloned = self.solution.cloneGraph(original)
        self.assertEqual(self.graph_to_adjList(cloned), adjList)

    def test_two_node_graph(self):
        adjList = [[2], [1]]
        original = self.build_graph(adjList)
        cloned = self.solution.cloneGraph(original)
        self.assertEqual(self.graph_to_adjList(cloned), adjList)


if __name__ == "__main__":
    unittest.main()
