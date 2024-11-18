import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_anagram_true(self):
        self.assertTrue(self.solution.isAnagram("anagram", "nagaram"))

    def test_anagram_false(self):
        self.assertFalse(self.solution.isAnagram("rat", "car"))

    def test_empty_strings(self):
        self.assertTrue(self.solution.isAnagram("", ""))

    def test_different_lengths(self):
        self.assertFalse(self.solution.isAnagram("a", "ab"))

    def test_same_characters_different_counts(self):
        self.assertFalse(self.solution.isAnagram("aabbcc", "aabbc"))


if __name__ == "__main__":
    unittest.main()
