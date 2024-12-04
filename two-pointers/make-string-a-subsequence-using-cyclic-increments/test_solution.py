import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        self.assertTrue(self.solution.canMakeSubsequence("abc", "ad"))

    def test_no_operation_needed(self):
        self.assertTrue(self.solution.canMakeSubsequence("abc", "ac"))

    def test_single_operation_needed(self):
        self.assertTrue(self.solution.canMakeSubsequence("xyz", "ya"))

    def test_multiple_operations_needed(self):
        self.assertTrue(self.solution.canMakeSubsequence("abcdef", "bdf"))

    def test_not_possible(self):
        self.assertFalse(self.solution.canMakeSubsequence("abc", "xyz"))

    def test_empty_str2(self):
        self.assertTrue(self.solution.canMakeSubsequence("abc", ""))

    def test_empty_str1(self):
        self.assertFalse(self.solution.canMakeSubsequence("", "a"))

    def test_same_strings(self):
        self.assertTrue(self.solution.canMakeSubsequence("abc", "abc"))

    def test_cyclic_wrap_around(self):
        self.assertTrue(self.solution.canMakeSubsequence("az", "ba"))


if __name__ == "__main__":
    unittest.main()
