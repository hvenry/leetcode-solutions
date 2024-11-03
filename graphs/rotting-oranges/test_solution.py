import unittest
from solution import Soluion


class TestRottingOranges(unittest.TestCase):
    def setUp(self):
        self.solution = Soluion()

    def test_example_case(self):
        grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
        self.assertEqual(self.solution.orangesRotting(grid), 4)

    def test_no_fresh_oranges(self):
        grid = [[2, 2, 0], [2, 2, 0], [0, 0, 0]]
        self.assertEqual(self.solution.orangesRotting(grid), 0)

    def test_no_rotten_oranges(self):
        grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.assertEqual(self.solution.orangesRotting(grid), -1)

    def test_single_rotten_orange(self):
        grid = [[0, 0, 0], [0, 2, 0], [0, 0, 0]]
        self.assertEqual(self.solution.orangesRotting(grid), 0)

    def test_single_fresh_orange(self):
        grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        self.assertEqual(self.solution.orangesRotting(grid), -1)


if __name__ == "__main__":
    unittest.main()
