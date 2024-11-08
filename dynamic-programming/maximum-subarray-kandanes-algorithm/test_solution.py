import unittest
from solution import Solution


class TestMaxSubArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_example_2(self):
        self.assertEqual(self.solution.maxSubArray([-2, 7, -3, 4]), 8)

    def test_all_negative(self):
        self.assertEqual(self.solution.maxSubArray([-1, -2, -3, -4]), -1)

    def test_single_element(self):
        self.assertEqual(self.solution.maxSubArray([1]), 1)
        self.assertEqual(self.solution.maxSubArray([-1]), -1)

    def test_mixed_elements(self):
        self.assertEqual(self.solution.maxSubArray([1, 2, 3, -2, 5]), 9)
        self.assertEqual(self.solution.maxSubArray([1, 2, -1, 2, -3, 2, -5]), 4)

    def test_large_input(self):
        self.assertEqual(self.solution.maxSubArray([100, -1, 100, -1, 100]), 298)


if __name__ == "__main__":
    unittest.main()
