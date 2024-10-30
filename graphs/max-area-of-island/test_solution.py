import unittest
from solution import Solution


class TestMaxAreaOfIsland(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        grid = [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 6)

    def test_no_island(self):
        grid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 0)

    def test_single_cell_island(self):
        grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 1)

    def test_multiple_islands(self):
        grid = [[1, 1, 0, 0, 0], [1, 0, 0, 1, 1], [0, 0, 0, 1, 1], [0, 1, 0, 0, 0]]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 4)

    def test_large_island(self):
        grid = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 20)


if __name__ == "__main__":
    unittest.main()
