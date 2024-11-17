import unittest
from solution import Solution


class TestShortestSubarray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        self.assertEqual(self.solution.shortestSubarray([2, -1, 2], 3), 3)

    def test_single_element(self):
        self.assertEqual(self.solution.shortestSubarray([1], 1), 1)
        self.assertEqual(self.solution.shortestSubarray([1], 2), -1)

    def test_all_positive(self):
        self.assertEqual(self.solution.shortestSubarray([1, 2, 3, 4, 5], 11), 3)
        self.assertEqual(self.solution.shortestSubarray([1, 2, 3, 4, 5], 15), 5)
        self.assertEqual(self.solution.shortestSubarray([1, 2, 3, 4, 5], 16), -1)

    def test_mixed_values(self):
        self.assertEqual(self.solution.shortestSubarray([-1, 2, -1, 2, 3], 3), 1)
        self.assertEqual(self.solution.shortestSubarray([-1, 2, 3, -2, 4], 5), 2)
        self.assertEqual(self.solution.shortestSubarray([2, -1, 2, -1, 2], 4), 5)

    def test_large_k(self):
        self.assertEqual(self.solution.shortestSubarray([1, 2, 3, 4, 5], 100), -1)
        self.assertEqual(self.solution.shortestSubarray([10, 20, 30, 40, 50], 100), 3)


if __name__ == "__main__":
    unittest.main()
