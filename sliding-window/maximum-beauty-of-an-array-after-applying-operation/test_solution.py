import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        nums = [4, 6, 1, 2]
        k = 2
        expected = 3
        result = self.solution.maximumBeauty(nums, k)
        self.assertEqual(result, expected)

    def test_all_elements_same(self):
        nums = [5, 5, 5, 5]
        k = 0
        expected = 4
        result = self.solution.maximumBeauty(nums, k)
        self.assertEqual(result, expected)

    def test_no_operations_needed(self):
        nums = [1, 2, 3, 4]
        k = 3
        expected = 4
        result = self.solution.maximumBeauty(nums, k)
        self.assertEqual(result, expected)

    def test_large_k(self):
        nums = [1, 3, 5, 7]
        k = 10
        expected = 4
        result = self.solution.maximumBeauty(nums, k)
        self.assertEqual(result, expected)

    def test_single_element(self):
        nums = [10]
        k = 5
        expected = 1
        result = self.solution.maximumBeauty(nums, k)
        self.assertEqual(result, expected)

    def test_no_possible_operations(self):
        nums = [1, 10, 20, 30]
        k = 1
        expected = 1
        result = self.solution.maximumBeauty(nums, k)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
