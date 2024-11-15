import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(self.solution.maxProfit(prices), 7)

    def test_example_2(self):
        prices = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.maxProfit(prices), 4)

    def test_example_3(self):
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(self.solution.maxProfit(prices), 0)

    def test_example_5(self):
        prices = [3, 3, 5, 0, 0, 3, 1, 4]
        self.assertEqual(self.solution.maxProfit(prices), 8)


if __name__ == "__main__":
    unittest.main()
