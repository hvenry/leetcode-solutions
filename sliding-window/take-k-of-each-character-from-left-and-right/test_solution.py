import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        self.assertEqual(self.solution.takeCharacters("aabaaaacaabc", 2), 8)

    def test_not_possible_case(self):
        self.assertEqual(self.solution.takeCharacters("abc", 2), -1)

    def test_minimum_k(self):
        self.assertEqual(self.solution.takeCharacters("abcabcabc", 1), 3)
        self.assertEqual(self.solution.takeCharacters("abcabcabc", 2), 6)
        self.assertEqual(self.solution.takeCharacters("abcabcabc", 3), 9)

    def test_large_input(self):
        s = "a" * 100000 + "b" * 100000 + "c" * 100000
        self.assertEqual(self.solution.takeCharacters(s, 100000), 300000)


if __name__ == "__main__":
    unittest.main()
