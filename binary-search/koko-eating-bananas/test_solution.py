import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        piles = [3, 6, 7, 11]
        h = 8
        self.assertEqual(self.solution.minEatingSpeed(piles, h), 4)

    def test_example2(self):
        piles = [30, 11, 23, 4, 20]
        h = 5
        self.assertEqual(self.solution.minEatingSpeed(piles, h), 30)

    def test_single_pile(self):
        piles = [100]
        h = 10
        self.assertEqual(self.solution.minEatingSpeed(piles, h), 10)

    def test_multiple_piles(self):
        piles = [3, 6, 7, 11, 15, 20]
        h = 10
        self.assertEqual(self.solution.minEatingSpeed(piles, h), 8)

    def test_minimum_hours(self):
        piles = [1, 2, 3, 4, 5]
        h = 5
        self.assertEqual(self.solution.minEatingSpeed(piles, h), 5)

    def test_maximum_hours(self):
        piles = [1, 2, 3, 4, 5]
        h = 15
        self.assertEqual(self.solution.minEatingSpeed(piles, h), 1)


if __name__ == "__main__":
    unittest.main()
