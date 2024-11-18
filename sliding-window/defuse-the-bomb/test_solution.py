import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_decrypt_positive_k(self):
        self.assertEqual(self.solution.decrypt([5, 7, 1, 4], 3), [12, 10, 16, 13])

    def test_decrypt_negative_k(self):
        self.assertEqual(self.solution.decrypt([2, 4, 9, 3], -2), [12, 5, 6, 13])

    def test_decrypt_zero_k(self):
        self.assertEqual(self.solution.decrypt([1, 2, 3, 4], 0), [0, 0, 0, 0])


if __name__ == "__main__":
    unittest.main()
