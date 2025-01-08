import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        words = ["mass", "as", "hero", "superhero"]
        expected = ["hero", "as"]
        self.assertCountEqual(self.solution.stringMatching(words), expected)

    def test_no_substrings(self):
        words = ["apple", "banana", "cherry"]
        expected = []
        self.assertCountEqual(self.solution.stringMatching(words), expected)

    def test_all_substrings(self):
        words = ["a", "ab", "abc", "abcd"]
        expected = ["a", "ab", "abc"]
        self.assertCountEqual(self.solution.stringMatching(words), expected)

    def test_single_word(self):
        words = ["word"]
        expected = []
        self.assertCountEqual(self.solution.stringMatching(words), expected)

    def test_duplicates(self):
        words = ["a", "a", "aa", "aaa"]
        expected = ["a", "a", "aa"]
        self.assertCountEqual(self.solution.stringMatching(words), expected)


if __name__ == "__main__":
    unittest.main()
