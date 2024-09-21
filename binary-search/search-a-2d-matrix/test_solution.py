import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_target_in_matrix(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 3
        self.assertTrue(self.solution.searchMatrix(matrix, target))

    def test_target_not_in_matrix(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 13
        self.assertFalse(self.solution.searchMatrix(matrix, target))

    def test_single_element_matrix_target_present(self):
        matrix = [[5]]
        target = 5
        self.assertTrue(self.solution.searchMatrix(matrix, target))

    def test_single_element_matrix_target_absent(self):
        matrix = [[5]]
        target = 1
        self.assertFalse(self.solution.searchMatrix(matrix, target))

    def test_target_in_first_row(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 7
        self.assertTrue(self.solution.searchMatrix(matrix, target))

    def test_target_in_last_row(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 34
        self.assertTrue(self.solution.searchMatrix(matrix, target))

    def test_target_in_last_element(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 60
        self.assertTrue(self.solution.searchMatrix(matrix, target))


if __name__ == "__main__":
    unittest.main()
