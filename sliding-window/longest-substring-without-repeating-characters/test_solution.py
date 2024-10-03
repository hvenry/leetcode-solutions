import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_empty_string(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring(""), 0)

    def test_single_character(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("a"), 1)

    def test_all_unique_characters(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcdef"), 6)

    def test_repeating_characters(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("bbbbb"), 1)

    def test_mixed_characters(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("pwwkew"), 3)

    def test_long_string(self):
        self.assertEqual(
            self.solution.lengthOfLongestSubstring("abcdeabcdeabcdeabcde"), 5
        )

    def test_special_characters(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("a!@#a!@#"), 4)

    def test_numbers_and_letters(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("123abc123"), 6)


if __name__ == "__main__":
    unittest.main()
