import unittest
from solution import Solution


class TestNetworkDelayTime(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
        n = 4
        k = 2
        self.assertEqual(self.solution.networkDelayTime(times, n, k), 2)

    def test_single_node(self):
        times = []
        n = 1
        k = 1
        self.assertEqual(self.solution.networkDelayTime(times, n, k), 0)

    def test_disconnected_graph(self):
        times = [[1, 2, 1], [2, 3, 2]]
        n = 4
        k = 1
        self.assertEqual(self.solution.networkDelayTime(times, n, k), -1)

    def test_multiple_paths(self):
        times = [[1, 2, 1], [2, 3, 2], [1, 3, 4]]
        n = 3
        k = 1
        self.assertEqual(self.solution.networkDelayTime(times, n, k), 3)


if __name__ == "__main__":
    unittest.main()
