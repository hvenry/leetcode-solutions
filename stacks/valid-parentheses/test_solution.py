import unittest
from solution import Solution


class testSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        s = "()[]{}"
        ans = True

        res = self.solution.isValid(s)
        self.assertEqual(ans, res)


if __name__ == "__main__":
    unittest.main()
