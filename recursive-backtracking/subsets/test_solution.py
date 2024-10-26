import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        nums = [1, 2, 3]
        expected_output = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
        result = self.solution.subsets(nums)
        self.assertEqual(sorted(result), sorted(expected_output))

    def test_empty_list(self):
        nums = []
        expected_output = [[]]
        result = self.solution.subsets(nums)
        self.assertEqual(result, expected_output)

    def test_single_element(self):
        nums = [1]
        expected_output = [[], [1]]
        result = self.solution.subsets(nums)
        self.assertEqual(result, expected_output)

    def test_two_elements(self):
        nums = [1, 2]
        expected_output = [[], [1], [2], [1, 2]]
        result = self.solution.subsets(nums)
        self.assertEqual(sorted(result), sorted(expected_output))

    def test_four_elements(self):
        nums = [1, 2, 3, 4]
        expected_output = [
            [],
            [1],
            [2],
            [3],
            [4],
            [1, 2],
            [1, 3],
            [1, 4],
            [2, 3],
            [2, 4],
            [3, 4],
            [1, 2, 3],
            [1, 2, 4],
            [1, 3, 4],
            [2, 3, 4],
            [1, 2, 3, 4],
        ]
        result = self.solution.subsets(nums)
        self.assertEqual(sorted(result), sorted(expected_output))


if __name__ == "__main__":
    unittest.main()
