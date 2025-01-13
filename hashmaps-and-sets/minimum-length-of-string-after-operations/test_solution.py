import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        self.assertEqual(self.solution.minimumLength("abaacbcbb"), 5)

    def test_single_character(self):
        self.assertEqual(self.solution.minimumLength("a"), 1)

    def test_all_unique_characters(self):
        self.assertEqual(self.solution.minimumLength("abcdef"), 6)

    def test_all_same_characters(self):
        self.assertEqual(self.solution.minimumLength("aaaaaa"), 2)

    def test_mixed_characters(self):
        self.assertEqual(self.solution.minimumLength("aabbcc"), 6)

    def test_empty_string(self):
        self.assertEqual(self.solution.minimumLength(""), 0)


if __name__ == "__main__":
    unittest.main()
