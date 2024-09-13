import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        nums = [-1, 0, 1, 2, -1, 4]
        ans = [[-1, -1, 2], [-1, 0, 1]]

        res = self.solution.threeSum(nums)
        self.assertEqual(res, ans)


if __name__ == "__main__":
    unittest.main()
