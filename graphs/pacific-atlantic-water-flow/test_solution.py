import unittest
from solution import Solution


class TestPacificAtlantic(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        heights = [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ]
        expected = [(0, 4), (1, 3), (1, 4), (2, 2), (3, 0), (3, 1), (4, 0)]
        result = self.solution.pacificAtlantic(heights)
        self.assertCountEqual(result, expected)

    def test_single_cell(self):
        heights = [[1]]
        expected = [(0, 0)]
        result = self.solution.pacificAtlantic(heights)
        self.assertCountEqual(result, expected)

    def test_flat_grid(self):
        heights = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        expected = [
            (0, 0),
            (0, 1),
            (0, 2),
            (1, 0),
            (1, 1),
            (1, 2),
            (2, 0),
            (2, 1),
            (2, 2),
        ]
        result = self.solution.pacificAtlantic(heights)
        self.assertCountEqual(result, expected)

    def test_increasing_diagonal(self):
        heights = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        expected = [(0, 2), (1, 2), (2, 0), (2, 1), (2, 2)]
        result = self.solution.pacificAtlantic(heights)
        self.assertCountEqual(result, expected)

    def test_decreasing_diagonal(self):
        heights = [[5, 4, 3], [4, 3, 2], [3, 2, 1]]
        expected = [(0, 0), (0, 1), (0, 2), (1, 0), (2, 0)]
        result = self.solution.pacificAtlantic(heights)
        self.assertCountEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
