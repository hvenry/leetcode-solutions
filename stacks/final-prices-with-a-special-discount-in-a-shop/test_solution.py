import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        prices = [8, 4, 6, 2, 3]
        expected = [4, 2, 4, 2, 3]
        self.assertEqual(self.solution.finalPrices(prices), expected)

    def test_no_discount(self):
        prices = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.finalPrices(prices), expected)

    def test_all_same_prices(self):
        prices = [5, 5, 5, 5, 5]
        expected = [0, 0, 0, 0, 5]
        self.assertEqual(self.solution.finalPrices(prices), expected)

    def test_single_item(self):
        prices = [10]
        expected = [10]
        self.assertEqual(self.solution.finalPrices(prices), expected)

    def test_decreasing_prices(self):
        prices = [10, 9, 8, 7, 6]
        expected = [1, 1, 1, 1, 6]
        self.assertEqual(self.solution.finalPrices(prices), expected)

    def test_increasing_prices(self):
        prices = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.finalPrices(prices), expected)


if __name__ == "__main__":
    unittest.main()
