import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        nums = [1, 2, 3, 4, 3, 2, 5]
        k = 3
        expected = [3, 4, -1, -1, -1]
        self.assertEqual(self.solution.resultsArray(nums, k), expected)

    def test_all_consecutive(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 4
        expected = [4, 5, 6, 7]
        self.assertEqual(self.solution.resultsArray(nums, k), expected)

    def test_no_consecutive(self):
        nums = [7, 1, 5, 3, 9, 2, 6]
        k = 2
        expected = [-1, -1, -1, -1, -1, -1]
        self.assertEqual(self.solution.resultsArray(nums, k), expected)

    def test_mixed_consecutive(self):
        nums = [1, 3, 2, 4, 5, 6, 8, 7]
        k = 3
        expected = [-1, -1, -1, 6, -1, -1]
        self.assertEqual(self.solution.resultsArray(nums, k), expected)

    def test_single_element(self):
        nums = [1]
        k = 1
        expected = [1]
        self.assertEqual(self.solution.resultsArray(nums, k), expected)

    def test_k_greater_than_length(self):
        nums = [1, 2, 3]
        k = 4
        expected = []
        self.assertEqual(self.solution.resultsArray(nums, k), expected)


if __name__ == "__main__":
    unittest.main()
