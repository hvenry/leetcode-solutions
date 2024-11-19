import unittest
from solution import Solution


class TestLongestConsecutiveSequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        nums = [100, 4, 200, 1, 3, 2]
        self.assertEqual(self.solution.longestConsecutive(nums), 4)

    def test_empty_array(self):
        nums = []
        self.assertEqual(self.solution.longestConsecutive(nums), 0)

    def test_single_element(self):
        nums = [1]
        self.assertEqual(self.solution.longestConsecutive(nums), 1)

    def test_no_consecutive_sequence(self):
        nums = [10, 5, 100]
        self.assertEqual(self.solution.longestConsecutive(nums), 1)

    def test_all_elements_same(self):
        nums = [2, 2, 2, 2]
        self.assertEqual(self.solution.longestConsecutive(nums), 1)

    def test_long_consecutive_sequence(self):
        nums = [1, 9, 3, 10, 4, 20, 2]
        self.assertEqual(self.solution.longestConsecutive(nums), 4)

    def test_negative_numbers(self):
        nums = [-1, -2, -3, -4, 0, 1, 2, 3]
        self.assertEqual(self.solution.longestConsecutive(nums), 8)

    def test_mixed_positive_and_negative(self):
        nums = [0, -1, 1, 2, -2, -3, 3, 4]
        self.assertEqual(self.solution.longestConsecutive(nums), 8)


if __name__ == "__main__":
    unittest.main()
