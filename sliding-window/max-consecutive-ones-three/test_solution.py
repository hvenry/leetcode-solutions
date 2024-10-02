import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
        k = 2
        expected = 6
        self.assertEqual(self.solution.longestOnes(nums, k), expected)

    def test_all_ones(self):
        nums = [1, 1, 1, 1, 1]
        k = 2
        expected = 5
        self.assertEqual(self.solution.longestOnes(nums, k), expected)

    def test_all_zeros(self):
        nums = [0, 0, 0, 0, 0]
        k = 3
        expected = 3
        self.assertEqual(self.solution.longestOnes(nums, k), expected)

    def test_no_flips_needed(self):
        nums = [1, 1, 1, 1, 0, 1, 1, 1, 1]
        k = 1
        expected = 9
        self.assertEqual(self.solution.longestOnes(nums, k), expected)

    def test_large_k(self):
        nums = [0, 0, 0, 0, 0]
        k = 5
        expected = 5
        self.assertEqual(self.solution.longestOnes(nums, k), expected)

    def test_no_flips_possible(self):
        nums = [0, 0, 0, 0, 0]
        k = 0
        expected = 0
        self.assertEqual(self.solution.longestOnes(nums, k), expected)


if __name__ == "__main__":
    unittest.main()
