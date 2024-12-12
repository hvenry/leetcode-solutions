import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        gifts = [25, 64, 9, 4, 100]
        k = 4
        self.assertEqual(self.solution.pickGifts(gifts, k), 29)

    def test_single_pile(self):
        gifts = [16]
        k = 2
        self.assertEqual(self.solution.pickGifts(gifts, k), 2)

    def test_no_operations(self):
        gifts = [10, 20, 30]
        k = 0
        self.assertEqual(self.solution.pickGifts(gifts, k), 60)

    def test_large_k(self):
        gifts = [1, 2, 3, 4, 5]
        k = 10
        self.assertEqual(self.solution.pickGifts(gifts, k), 5)


if __name__ == "__main__":
    unittest.main()
