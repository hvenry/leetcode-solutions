import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        nums = [2, 1, 3, 4, 5, 2]
        expected = 7
        self.assertEqual(self.solution.findScore(nums), expected)

    def test_single_element(self):
        nums = [10]
        expected = 10
        self.assertEqual(self.solution.findScore(nums), expected)

    def test_already_sorted(self):
        nums = [1, 2, 3, 4, 5]
        expected = 9
        self.assertEqual(self.solution.findScore(nums), expected)

    def test_reverse_sorted(self):
        nums = [5, 4, 3, 2, 1]
        expected = 9
        self.assertEqual(self.solution.findScore(nums), expected)

    def test_large_numbers(self):
        nums = [1000, 2000, 3000, 4000, 5000]
        expected = 9000
        self.assertEqual(self.solution.findScore(nums), expected)

    def test_with_gaps(self):
        nums = [1, 3, 5, 7, 9]
        expected = 15
        self.assertEqual(self.solution.findScore(nums), expected)


if __name__ == "__main__":
    unittest.main()
