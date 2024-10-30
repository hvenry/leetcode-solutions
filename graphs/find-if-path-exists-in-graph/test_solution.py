import unittest
from solution import Solution


class TestValidPath(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        n = 3
        edges = [[0, 1], [1, 2], [2, 0]]
        source = 0
        destination = 2
        self.assertTrue(self.solution.validPath(n, edges, source, destination))

    def test_example_2(self):
        n = 6
        edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
        source = 0
        destination = 5
        self.assertFalse(self.solution.validPath(n, edges, source, destination))

    def test_single_node(self):
        n = 1
        edges = []
        source = 0
        destination = 0
        self.assertTrue(self.solution.validPath(n, edges, source, destination))

    def test_disconnected_graph(self):
        n = 4
        edges = [[0, 1], [2, 3]]
        source = 0
        destination = 3
        self.assertFalse(self.solution.validPath(n, edges, source, destination))


if __name__ == "__main__":
    unittest.main()
