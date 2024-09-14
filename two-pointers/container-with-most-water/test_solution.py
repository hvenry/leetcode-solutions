import unittest
from solution import Solution


class testSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        ans = 49

        res = self.solution.maxArea(height)
        self.assertEqual(res, ans)


if __name__ == "__main__":
    unittest.main()
