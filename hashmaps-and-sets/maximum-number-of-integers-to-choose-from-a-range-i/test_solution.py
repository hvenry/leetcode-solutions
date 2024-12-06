import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        banned = [1, 6, 5]
        n = 5
        maxSum = 6
        self.assertEqual(self.solution.maxCount(banned, n, maxSum), 2)

    def test_no_banned_numbers(self):
        banned = []
        n = 5
        maxSum = 10
        self.assertEqual(self.solution.maxCount(banned, n, maxSum), 4)

    def test_all_numbers_banned(self):
        banned = [1, 2, 3, 4, 5]
        n = 5
        maxSum = 10
        self.assertEqual(self.solution.maxCount(banned, n, maxSum), 0)

    def test_maxSum_too_small(self):
        banned = [2, 4]
        n = 5
        maxSum = 1
        self.assertEqual(self.solution.maxCount(banned, n, maxSum), 1)


if __name__ == "__main__":
    unittest.main()
