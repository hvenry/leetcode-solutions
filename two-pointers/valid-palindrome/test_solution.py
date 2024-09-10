import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        s = "A man, a plan, a canal: Panama"
        ans = True

        res = self.solution.isPalindrome(s)
        self.assertEqual(res, ans)


if __name__ == "__main__":
    unittest.main()
