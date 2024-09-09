import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        nums = [-4, -1, 0, 3, 10]
        ans = [0, 1, 9, 16, 100]

        res = self.solution.sortedSquares(nums)
        self.assertEqual(res, ans)


if __name__ == "__main__":
    unittest.main()
