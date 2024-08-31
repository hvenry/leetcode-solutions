import unittest
import unittest.main
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        nums = [2, 7, 11, 15]
        target = 9
        ans = [0, 1]

        res = self.solution.twoSum(nums, target)
        self.assertEqual(res, ans)


if __name__ == "__main__":
    unittest.main()
