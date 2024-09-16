import unittest
from solution import Solution


class testSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        tokens = ["2", "1", "+", "3", "*"]
        ans = 9

        res = self.solution.evalRPN(tokens)
        self.assertEqual(res, ans)


if __name__ == "__main__":
    unittest.main()
