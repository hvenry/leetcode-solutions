import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        ans = [[1, 6], [8, 10], [15, 18]]

        res = self.solution.merge(intervals)

        self.assertEqual(ans, res)


if __name__ == "__main__":
    unittest.main()
