import unittest
from solution import Solution


class TestCombinationSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        candidates = [2, 3, 6, 7]
        target = 7
        expected_output = [[2, 2, 3], [7]]
        self.assertCountEqual(
            self.solution.combinationSum(candidates, target), expected_output
        )

    def test_example2(self):
        candidates = [2, 3, 5]
        target = 8
        expected_output = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        self.assertCountEqual(
            self.solution.combinationSum(candidates, target), expected_output
        )

    def test_empty_candidates(self):
        candidates = []
        target = 7
        expected_output = []
        self.assertCountEqual(
            self.solution.combinationSum(candidates, target), expected_output
        )

    def test_no_combination(self):
        candidates = [2, 4, 6]
        target = 5
        expected_output = []
        self.assertCountEqual(
            self.solution.combinationSum(candidates, target), expected_output
        )

    def test_single_candidate(self):
        candidates = [7]
        target = 7
        expected_output = [[7]]
        self.assertCountEqual(
            self.solution.combinationSum(candidates, target), expected_output
        )

    def test_large_target(self):
        candidates = [2, 3, 5]
        target = 10
        expected_output = [[2, 2, 2, 2, 2], [2, 2, 3, 3], [2, 3, 5], [5, 5]]
        self.assertCountEqual(
            self.solution.combinationSum(candidates, target), expected_output
        )


if __name__ == "__main__":
    unittest.main()
