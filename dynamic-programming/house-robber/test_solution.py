import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.rob([1, 2, 3, 1]), 4)

    def test_example2(self):
        self.assertEqual(self.solution.rob([2, 7, 9, 3, 1]), 12)

    def test_single_house(self):
        self.assertEqual(self.solution.rob([5]), 5)

    def test_two_houses(self):
        self.assertEqual(self.solution.rob([2, 3]), 3)

    def test_all_houses_same_value(self):
        self.assertEqual(self.solution.rob([4, 4, 4, 4, 4]), 12)

    def test_alternating_values(self):
        self.assertEqual(self.solution.rob([2, 1, 1, 2]), 4)

    def test_large_values(self):
        self.assertEqual(self.solution.rob([100, 200, 300, 400, 500]), 900)


if __name__ == "__main__":
    unittest.main()
