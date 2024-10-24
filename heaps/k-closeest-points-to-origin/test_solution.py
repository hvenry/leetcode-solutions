import unittest
from solution import Solution


class TestKClosestPoints(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        points = [[1, 3], [-2, 2]]
        k = 1
        expected = [(-2, 2)]
        result = self.solution.kClosest(points, k)
        self.assertCountEqual(result, expected)

    def test_example_2(self):
        points = [[3, 3], [2, 2], [4, 4], [1, 1]]
        k = 2
        expected = [(1, 1), (2, 2)]
        result = self.solution.kClosest(points, k)
        self.assertCountEqual(result, expected)

    def test_all_points(self):
        points = [[1, 2], [3, 4], [5, 6]]
        k = 3
        expected = [(1, 2), (3, 4), (5, 6)]
        result = self.solution.kClosest(points, k)
        self.assertCountEqual(result, expected)

    def test_k_greater_than_points(self):
        points = [[1, 2], [3, 4]]
        k = 5
        expected = [(1, 2), (3, 4)]
        result = self.solution.kClosest(points, k)
        self.assertCountEqual(result, expected)

    def test_single_point(self):
        points = [[1, 2]]
        k = 1
        expected = [(1, 2)]
        result = self.solution.kClosest(points, k)
        self.assertCountEqual(result, expected)

    def test_no_points(self):
        points = []
        k = 1
        expected = []
        result = self.solution.kClosest(points, k)
        self.assertCountEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
