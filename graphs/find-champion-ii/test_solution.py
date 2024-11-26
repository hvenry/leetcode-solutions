import unittest
from solution import Solution


class TestFindChampion(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        n = 3
        edges = [[0, 1], [1, 2]]
        self.assertEqual(self.solution.findChampion(n, edges), 0)

    def test_example_2(self):
        n = 4
        edges = [[0, 2], [1, 3], [1, 2]]
        self.assertEqual(self.solution.findChampion(n, edges), -1)

    def test_no_edges(self):
        n = 3
        edges = []
        self.assertEqual(self.solution.findChampion(n, edges), -1)

    def test_single_node(self):
        n = 1
        edges = []
        self.assertEqual(self.solution.findChampion(n, edges), 0)

    def test_multiple_champions(self):
        n = 5
        edges = [[0, 2], [1, 2], [3, 4]]
        self.assertEqual(self.solution.findChampion(n, edges), -1)

    def test_complex_graph(self):
        n = 6
        edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]
        self.assertEqual(self.solution.findChampion(n, edges), 0)

    def test_disconnected_graph(self):
        n = 6
        edges = [[0, 1], [2, 3], [4, 5]]
        self.assertEqual(self.solution.findChampion(n, edges), -1)


if __name__ == "__main__":
    unittest.main()
