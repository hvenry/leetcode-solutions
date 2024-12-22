import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        heights = [6, 4, 8, 5, 2, 7]
        queries = [[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]]
        expected = [2, 5, -1, 5, 2]
        self.assertEqual(
            self.solution.leftmostBuildingQueries(heights, queries), expected
        )

    def test_single_building(self):
        heights = [5]
        queries = [[0, 0]]
        expected = [0]
        self.assertEqual(
            self.solution.leftmostBuildingQueries(heights, queries), expected
        )

    def test_no_possible_meeting(self):
        heights = [1, 2, 3, 4, 5]
        queries = [[0, 4], [1, 3], [2, 2]]
        expected = [4, 3, 2]
        self.assertEqual(
            self.solution.leftmostBuildingQueries(heights, queries), expected
        )

    def test_large_heights(self):
        heights = [100, 200, 300, 400, 500]
        queries = [[0, 1], [1, 2], [2, 3], [3, 4], [0, 4]]
        expected = [1, 2, 3, 4, 4]
        self.assertEqual(
            self.solution.leftmostBuildingQueries(heights, queries), expected
        )


if __name__ == "__main__":
    unittest.main()
