import unittest
from solution import Solution


class TestLongestCommonSubsequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        text1 = "abcde"
        text2 = "ace"
        self.assertEqual(self.solution.longestCommonSubsequence(text1, text2), 3)

    def test_example2(self):
        text1 = "abc"
        text2 = "abc"
        self.assertEqual(self.solution.longestCommonSubsequence(text1, text2), 3)

    def test_example3(self):
        text1 = "abc"
        text2 = "def"
        self.assertEqual(self.solution.longestCommonSubsequence(text1, text2), 0)

    def test_empty_strings(self):
        text1 = ""
        text2 = ""
        self.assertEqual(self.solution.longestCommonSubsequence(text1, text2), 0)

    def test_one_empty_string(self):
        text1 = "abc"
        text2 = ""
        self.assertEqual(self.solution.longestCommonSubsequence(text1, text2), 0)

    def test_long_strings(self):
        text1 = "abcdefghijklmnopqrstuvwxyz"
        text2 = "acegikmoqsuwy"
        self.assertEqual(self.solution.longestCommonSubsequence(text1, text2), 13)


if __name__ == "__main__":
    unittest.main()
