import unittest
from solution import Solution


class TestValidParentheses(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_parentheses(self):
        self.assertTrue(self.solution.isValid("()[]{}"))
        self.assertTrue(self.solution.isValid("()"))
        self.assertTrue(self.solution.isValid("{[]}"))
        self.assertTrue(self.solution.isValid(""))

    def test_invalid_parentheses(self):
        self.assertFalse(self.solution.isValid("(]"))
        self.assertFalse(self.solution.isValid("([)]"))
        self.assertFalse(self.solution.isValid("((("))
        self.assertFalse(self.solution.isValid("]"))


if __name__ == "__main__":
    unittest.main()
