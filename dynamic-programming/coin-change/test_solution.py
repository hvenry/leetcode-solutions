import unittest
from solution import Solution


class TestCoinChange(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        self.assertEqual(self.solution.coinChange([1, 2, 5], 11), 3)

    def test_no_solution(self):
        self.assertEqual(self.solution.coinChange([2], 3), -1)

    def test_single_coin(self):
        self.assertEqual(self.solution.coinChange([1], 0), 0)
        self.assertEqual(self.solution.coinChange([1], 1), 1)
        self.assertEqual(self.solution.coinChange([1], 2), 2)

    def test_multiple_coins(self):
        self.assertEqual(self.solution.coinChange([1, 2, 5], 100), 20)
        self.assertEqual(self.solution.coinChange([1, 3, 4, 5], 7), 2)

    def test_large_coins(self):
        self.assertEqual(self.solution.coinChange([186, 419, 83, 408], 6249), 20)


if __name__ == "__main__":
    unittest.main()
