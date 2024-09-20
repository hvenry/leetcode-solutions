import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_perfect_square(self):
        self.assertTrue(self.solution.isPerfectSquare(16))
        self.assertTrue(self.solution.isPerfectSquare(1))
        self.assertTrue(self.solution.isPerfectSquare(4))
        self.assertTrue(self.solution.isPerfectSquare(9))
        self.assertTrue(self.solution.isPerfectSquare(25))
        self.assertTrue(self.solution.isPerfectSquare(100))

    def test_not_perfect_square(self):
        self.assertFalse(self.solution.isPerfectSquare(14))
        self.assertFalse(self.solution.isPerfectSquare(2))
        self.assertFalse(self.solution.isPerfectSquare(3))
        self.assertFalse(self.solution.isPerfectSquare(10))
        self.assertFalse(self.solution.isPerfectSquare(26))
        self.assertFalse(self.solution.isPerfectSquare(99))

    def test_large_numbers(self):
        self.assertTrue(self.solution.isPerfectSquare(100000000))
        self.assertFalse(self.solution.isPerfectSquare(100000001))


if __name__ == "__main__":
    unittest.main()
