import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        nums = [1, 12, -5, -6, 50, 3]
        k = 4
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 12.75, places=5)

    def test_all_positive_numbers(self):
        nums = [5, 5, 5, 5, 5]
        k = 3
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 5.0, places=5)

    def test_all_negative_numbers(self):
        nums = [-1, -2, -3, -4, -5]
        k = 2
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, -1.5, places=5)

    def test_mixed_numbers(self):
        nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]
        k = 5
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 3.0, places=5)

    def test_single_element(self):
        nums = [10]
        k = 1
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 10.0, places=5)

    def test_large_k(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        k = 10
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 5.5, places=5)


if __name__ == "__main__":
    unittest.main()
