import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        numbers = [2, 7, 11, 15]
        target = 9
        ans = [1, 2]

        res = self.solution.twoSum(numbers, target)
        self.assertEqual(res, ans)


if __name__ == "__main__":
    unittest.main()
