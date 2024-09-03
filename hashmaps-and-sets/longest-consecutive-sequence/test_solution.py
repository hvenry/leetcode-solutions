import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        nums = [100, 4, 200, 1, 3, 2]
        ans = 4

        res = self.solution.longestConsecutive(nums)
        self.assertEqual(res, ans)


if __name__ == "__main__":
    unittest.main()
