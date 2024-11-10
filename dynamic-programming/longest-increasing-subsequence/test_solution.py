import unittest
from solution import Solution


class TestLengthOfLIS(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        self.assertEqual(self.solution.lengthOfLIS(nums), 4)

    def test_increasing_sequence(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.lengthOfLIS(nums), 5)

    def test_decreasing_sequence(self):
        nums = [5, 4, 3, 2, 1]
        self.assertEqual(self.solution.lengthOfLIS(nums), 1)

    def test_mixed_sequence(self):
        nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
        self.assertEqual(self.solution.lengthOfLIS(nums), 6)

    def test_single_element(self):
        nums = [10]
        self.assertEqual(self.solution.lengthOfLIS(nums), 1)

    def test_duplicate_elements(self):
        nums = [2, 2, 2, 2, 2]
        self.assertEqual(self.solution.lengthOfLIS(nums), 1)


if __name__ == "__main__":
    unittest.main()
