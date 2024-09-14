import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_trap(self):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        ans = 6

        res = self.solution.trap(height)
        self.assertEqual(res, ans)


if __name__ == "__main__":
    unittest.main()