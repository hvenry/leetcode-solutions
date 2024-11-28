import unittest
from solution import Solution


class TestMinimumObstacles(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        grid = [[0, 1, 1], [1, 1, 0], [1, 1, 0]]
        self.assertEqual(self.solution.minimumObstacles(grid), 2)

    def test_no_obstacles(self):
        grid = [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]]
        self.assertEqual(self.solution.minimumObstacles(grid), 0)


if __name__ == "__main__":
    unittest.main()
