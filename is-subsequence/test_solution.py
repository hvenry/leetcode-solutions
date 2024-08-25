import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        s = "abc"
        t = "ahbgdc"

        res = self.solution.isSubsequence(s, t)
        self.assertEqual(res, True)


if __name__ == "__main__":
    unittest.main()
