import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        nums = [1, 5, 4, 2, 9, 9, 9]
        k = 3
        self.assertEqual(self.solution.maximumSubarraySum(nums, k), 15)

    def test_no_valid_subarray(self):
        nums = [1, 1, 1, 1, 1]
        k = 2
        self.assertEqual(self.solution.maximumSubarraySum(nums, k), 0)

    def test_all_elements_unique(self):
        nums = [1, 2, 3, 4, 5]
        k = 3
        self.assertEqual(self.solution.maximumSubarraySum(nums, k), 12)

    def test_subarray_at_end(self):
        nums = [4, 2, 1, 6, 5]
        k = 2
        self.assertEqual(self.solution.maximumSubarraySum(nums, k), 11)

    def test_single_element_subarray(self):
        nums = [10, 20, 30, 40, 50]
        k = 1
        self.assertEqual(self.solution.maximumSubarraySum(nums, k), 50)

    def test_large_k(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        k = 10
        self.assertEqual(self.solution.maximumSubarraySum(nums, k), 55)


if __name__ == "__main__":
    unittest.main()
