import unittest
from solution import Solution


class TestMinCostConnectPoints(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 20)

    def test_single_point(self):
        points = [[0, 0]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 0)

    def test_two_points(self):
        points = [[0, 0], [1, 1]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 2)

    def test_four_points(self):
        points = [[0, 0], [1, 1], [1, 0], [0, 1]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 3)

    def test_large_coordinates(self):
        points = [[-1000000, -1000000], [1000000, 1000000]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 4000000)

    def test_negative_coordinates(self):
        points = [[-1, -1], [-2, -2], [-3, -3]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 4)


if __name__ == "__main__":
    unittest.main()
