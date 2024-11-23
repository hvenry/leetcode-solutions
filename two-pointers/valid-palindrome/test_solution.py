import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_palindrome(self):
        self.assertTrue(self.solution.isPalindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(self.solution.isPalindrome("racecar"))
        self.assertTrue(self.solution.isPalindrome(""))

    def test_invalid_palindrome(self):
        self.assertFalse(self.solution.isPalindrome("hello"))
        self.assertFalse(self.solution.isPalindrome("race a car"))

    def test_mixed_cases(self):
        self.assertTrue(self.solution.isPalindrome("No 'x' in Nixon"))
        self.assertTrue(self.solution.isPalindrome("Able was I ere I saw Elba"))

    def test_numeric_palindrome(self):
        self.assertTrue(self.solution.isPalindrome("12321"))
        self.assertFalse(self.solution.isPalindrome("12345"))


if __name__ == "__main__":
    unittest.main()
