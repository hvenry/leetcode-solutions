import unittest
from solution import Solution


class TestCharacterReplacement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.characterReplacement("ABAB", 2), 4)

    def test_example2(self):
        self.assertEqual(self.solution.characterReplacement("AABABBA", 1), 4)

    def test_all_same_characters(self):
        self.assertEqual(self.solution.characterReplacement("AAAA", 2), 4)

    def test_no_replacements_needed(self):
        self.assertEqual(self.solution.characterReplacement("AABBB", 0), 3)

    def test_single_character(self):
        self.assertEqual(self.solution.characterReplacement("A", 1), 1)

    def test_empty_string(self):
        self.assertEqual(self.solution.characterReplacement("", 2), 0)

    def test_large_k(self):
        self.assertEqual(self.solution.characterReplacement("ABCDE", 10), 5)

    def test_mixed_characters(self):
        self.assertEqual(self.solution.characterReplacement("ABACCC", 2), 5)


if __name__ == "__main__":
    unittest.main()
