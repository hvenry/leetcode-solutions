import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        jewels = "aA"
        stones = "aAAbbbb"
        ans = 3

        res = self.solution.numJewelsInStones(jewels, stones)
        self.assertEqual(res, ans)


if __name__ == "__main__":
    unittest.main()
