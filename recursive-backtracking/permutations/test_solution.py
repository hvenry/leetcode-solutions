import unittest
from solution import Solution


class TestPermutations(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_permutations_example1(self):
        nums = [1, 2, 3]
        expected_output = [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1],
        ]
        result = self.solution.permute(nums)
        self.assertEqual(sorted(result), sorted(expected_output))

    def test_permutations_example2(self):
        nums = [0, 1]
        expected_output = [[0, 1], [1, 0]]
        result = self.solution.permute(nums)
        self.assertEqual(sorted(result), sorted(expected_output))

    def test_permutations_single_element(self):
        nums = [1]
        expected_output = [[1]]
        result = self.solution.permute(nums)
        self.assertEqual(result, expected_output)

    def test_permutations_empty(self):
        nums = []
        expected_output = [[]]
        result = self.solution.permute(nums)
        self.assertEqual(result, expected_output)

    def test_permutations_four_elements(self):
        nums = [1, 2, 3, 4]
        expected_output = [
            [1, 2, 3, 4],
            [1, 2, 4, 3],
            [1, 3, 2, 4],
            [1, 3, 4, 2],
            [1, 4, 2, 3],
            [1, 4, 3, 2],
            [2, 1, 3, 4],
            [2, 1, 4, 3],
            [2, 3, 1, 4],
            [2, 3, 4, 1],
            [2, 4, 1, 3],
            [2, 4, 3, 1],
            [3, 1, 2, 4],
            [3, 1, 4, 2],
            [3, 2, 1, 4],
            [3, 2, 4, 1],
            [3, 4, 1, 2],
            [3, 4, 2, 1],
            [4, 1, 2, 3],
            [4, 1, 3, 2],
            [4, 2, 1, 3],
            [4, 2, 3, 1],
            [4, 3, 1, 2],
            [4, 3, 2, 1],
        ]
        result = self.solution.permute(nums)
        self.assertEqual(sorted(result), sorted(expected_output))


if __name__ == "__main__":
    unittest.main()
