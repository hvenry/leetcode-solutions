import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        self.assertEqual(self.solution.countPalindromicSubsequence("aabca"), 3)

    def test_single_character(self):
        self.assertEqual(self.solution.countPalindromicSubsequence("a"), 0)

    def test_no_palindromes(self):
        self.assertEqual(self.solution.countPalindromicSubsequence("abc"), 0)

    def test_all_same_characters(self):
        self.assertEqual(self.solution.countPalindromicSubsequence("aaa"), 1)

    def test_mixed_characters(self):
        self.assertEqual(self.solution.countPalindromicSubsequence("abacaba"), 5)

    def test_long_string(self):
        self.assertEqual(
            self.solution.countPalindromicSubsequence("abcdefghijklmnopqrstuvwxyz"), 0
        )

    def test_repeated_characters(self):
        self.assertEqual(self.solution.countPalindromicSubsequence("aabbcc"), 0)


if __name__ == "__main__":
    unittest.main()
