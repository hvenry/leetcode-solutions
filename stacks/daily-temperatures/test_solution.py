import unittest
from solution import Solution


class testSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
        ans = [1, 1, 4, 2, 1, 1, 0, 0]

        res = self.solution.dailyTemperatures(temperatures)
        self.assertEqual(res, ans)


if __name__ == "__main__":
    unittest.main()
