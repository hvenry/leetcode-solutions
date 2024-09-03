import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        text = "nlaebolko"
        ans = 1

        res = self.solution.maxNumberOfBalloons(text)

        self.assertEqual(res, ans)


if __name__ == "__main__":
    unittest.main()
