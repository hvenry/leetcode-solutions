import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        self.assertEqual(self.solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]), 2)

    def test_no_subarray(self):
        self.assertEqual(self.solution.minSubArrayLen(100, [1, 2, 3, 4, 5]), 0)

    def test_single_element_equal_to_target(self):
        self.assertEqual(self.solution.minSubArrayLen(4, [4]), 1)

    def test_single_element_less_than_target(self):
        self.assertEqual(self.solution.minSubArrayLen(5, [4]), 0)

    def test_all_elements_sum_to_target(self):
        self.assertEqual(self.solution.minSubArrayLen(15, [1, 2, 3, 4, 5]), 5)

    def test_multiple_subarrays(self):
        self.assertEqual(self.solution.minSubArrayLen(11, [1, 2, 3, 4, 5]), 3)


if __name__ == "__main__":
    unittest.main()
