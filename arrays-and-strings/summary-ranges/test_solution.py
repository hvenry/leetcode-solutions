import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        nums = [0, 1, 2, 4, 5, 7]
        res = self.solution.summaryRanges(nums)
        self.assertEqual(res, ["0->2", "4->5", "7"])


if __name__ == "__main__":
    unittest.main()
