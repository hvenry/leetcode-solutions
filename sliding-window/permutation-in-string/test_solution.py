import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertTrue(self.solution.checkInclusion("ab", "eidbaooo"))

    def test_example2(self):
        self.assertFalse(self.solution.checkInclusion("ab", "eidboaoo"))

    def test_empty_s1(self):
        self.assertTrue(self.solution.checkInclusion("", "eidbaooo"))

    def test_empty_s2(self):
        self.assertFalse(self.solution.checkInclusion("ab", ""))

    def test_s1_longer_than_s2(self):
        self.assertFalse(self.solution.checkInclusion("abcd", "abc"))

    def test_no_permutation(self):
        self.assertFalse(self.solution.checkInclusion("abc", "defghijkl"))

    def test_permutation_at_start(self):
        self.assertTrue(self.solution.checkInclusion("abc", "cbadef"))

    def test_permutation_at_end(self):
        self.assertTrue(self.solution.checkInclusion("abc", "defcba"))

    def test_permutation_in_middle(self):
        self.assertTrue(self.solution.checkInclusion("abc", "defcbagh"))

    def test_repeated_characters(self):
        self.assertTrue(self.solution.checkInclusion("aabb", "bbbaaac"))

    def test_single_character(self):
        self.assertTrue(self.solution.checkInclusion("a", "a"))
        self.assertFalse(self.solution.checkInclusion("a", "b"))


if __name__ == "__main__":
    unittest.main()
