import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        matrix = [[0, 1], [1, 1]]
        self.assertEqual(self.solution.maxEqualRowsAfterFlips(matrix), 1)

    def test_example2(self):
        matrix = [[0, 1], [1, 0]]
        self.assertEqual(self.solution.maxEqualRowsAfterFlips(matrix), 2)

    def test_all_zeros(self):
        matrix = [[0, 0], [0, 0]]
        self.assertEqual(self.solution.maxEqualRowsAfterFlips(matrix), 2)

    def test_all_ones(self):
        matrix = [[1, 1], [1, 1]]
        self.assertEqual(self.solution.maxEqualRowsAfterFlips(matrix), 2)

    def test_single_row(self):
        matrix = [[0, 1, 0, 1]]
        self.assertEqual(self.solution.maxEqualRowsAfterFlips(matrix), 1)


if __name__ == "__main__":
    unittest.main()
