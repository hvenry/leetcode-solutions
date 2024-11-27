import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        n = 5
        queries = [[2, 4], [0, 2], [0, 4]]
        expected = [3, 2, 1]
        self.assertEqual(
            self.solution.shortestDistanceAfterQueries(n, queries), expected
        )

    def test_example_case_2(self):
        n = 4
        queries = [[0, 3], [0, 2]]
        expected = [1, 1]
        self.assertEqual(
            self.solution.shortestDistanceAfterQueries(n, queries), expected
        )


if __name__ == "__main__":
    unittest.main()
