import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        self.assertEqual(self.solution.maximumLenght("aaaa"), 2)

    def test_no_special_substring(self):
        self.assertEqual(self.solution.maximumLenght("abc"), -1)

    def test_single_character(self):
        self.assertEqual(self.solution.maximumLenght("a"), -1)

    def test_multiple_special_substrings(self):
        self.assertEqual(self.solution.maximumLenght("aaabbbccc"), 1)

    def test_long_special_substring(self):
        self.assertEqual(self.solution.maximumLenght("aaaabbbbcccc"), 2)

    def test_special_substring_at_edges(self):
        self.assertEqual(self.solution.maximumLenght("aaaxaaaxaaax"), 4)


if __name__ == "__main__":
    unittest.main()
