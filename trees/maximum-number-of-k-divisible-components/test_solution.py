import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        n = 7
        edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]
        values = [3, 0, 6, 1, 5, 2, 1]
        k = 3
        self.assertEqual(self.solution.maxKDivisibleComponents(n, edges, values, k), 3)

    def test_single_node(self):
        n = 1
        edges = []
        values = [3]
        k = 3
        self.assertEqual(self.solution.maxKDivisibleComponents(n, edges, values, k), 1)

    def test_all_nodes_divisible(self):
        n = 4
        edges = [[0, 1], [1, 2], [2, 3]]
        values = [4, 8, 12, 16]
        k = 4
        self.assertEqual(self.solution.maxKDivisibleComponents(n, edges, values, k), 4)

    def test_complex_case(self):
        n = 5
        edges = [[0, 1], [0, 2], [1, 3], [1, 4]]
        values = [5, 10, 15, 20, 25]
        k = 5
        self.assertEqual(self.solution.maxKDivisibleComponents(n, edges, values, k), 5)


if __name__ == "__main__":
    unittest.main()
