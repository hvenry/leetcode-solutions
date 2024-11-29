import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        grid = [[0, 1, 3, 2], [5, 1, 2, 5], [4, 3, 8, 6]]
        self.assertEqual(self.solution.minimumTime(grid), 7)

    def test_no_possible_path(self):
        grid = [[0, 2], [2, 0]]
        self.assertEqual(self.solution.minimumTime(grid), -1)

    def test_large_grid(self):
        grid = [
            [0, 1, 2, 3, 4],
            [1, 2, 3, 4, 5],
            [2, 3, 4, 5, 6],
            [3, 4, 5, 6, 7],
            [4, 5, 6, 7, 8],
        ]
        self.assertEqual(self.solution.minimumTime(grid), 8)

    def test_path_with_waiting(self):
        grid = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.assertEqual(self.solution.minimumTime(grid), 8)


if __name__ == "__main__":
    unittest.main()
