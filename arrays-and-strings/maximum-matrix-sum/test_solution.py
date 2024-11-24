import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        matrix = [[1, -1], [-1, 1]]
        self.assertEqual(self.solution.maxMatrixSum(matrix), 4)

    def test_example2(self):
        matrix = [[1, 2, 3], [-1, -2, -3], [1, 2, 3]]
        self.assertEqual(self.solution.maxMatrixSum(matrix), 16)

    def test_all_positive(self):
        matrix = [[1, 2], [3, 4]]
        self.assertEqual(self.solution.maxMatrixSum(matrix), 10)

    def test_all_negative(self):
        matrix = [[-1, -2], [-3, -4]]
        self.assertEqual(self.solution.maxMatrixSum(matrix), 10)

    def test_mixed_values(self):
        matrix = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
        self.assertEqual(self.solution.maxMatrixSum(matrix), 45)

    def test_single_element_positive(self):
        matrix = [[5]]
        self.assertEqual(self.solution.maxMatrixSum(matrix), 5)

    def test_single_element_negative(self):
        matrix = [[-5]]
        self.assertEqual(self.solution.maxMatrixSum(matrix), 5)

    def test_large_matrix(self):
        matrix = [[1, -2, 3, -4], [-5, 6, -7, 8], [9, -10, 11, -12], [-13, 14, -15, 16]]
        self.assertEqual(self.solution.maxMatrixSum(matrix), 136)


if __name__ == "__main__":
    unittest.main()
