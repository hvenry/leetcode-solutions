import unittest
from solution import Solution


class TestNumIslands(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_island(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        self.assertEqual(self.solution.numIslands(grid), 1)

    def test_multiple_islands(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        self.assertEqual(self.solution.numIslands(grid), 3)

    def test_no_islands(self):
        grid = [
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        self.assertEqual(self.solution.numIslands(grid), 0)

    def test_all_land(self):
        grid = [
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
        ]
        self.assertEqual(self.solution.numIslands(grid), 1)

    def test_single_cell_island(self):
        grid = [
            ["0", "0", "0", "0", "0"],
            ["0", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        self.assertEqual(self.solution.numIslands(grid), 1)


if __name__ == "__main__":
    unittest.main()
