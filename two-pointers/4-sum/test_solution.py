import unittest
from solution import Solution


class TestFourSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [1, 0, -1, 0, -2, 2]
        target = 0
        expected = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        result = self.solution.fourSum(nums, target)
        self.assertEqual(sorted(result), sorted(expected))

    def test_example2(self):
        nums = [2, 2, 2, 2, 2]
        target = 8
        expected = [[2, 2, 2, 2]]
        result = self.solution.fourSum(nums, target)
        self.assertEqual(result, expected)

    def test_no_solution(self):
        nums = [1, 2, 3, 4]
        target = 100
        expected = []
        result = self.solution.fourSum(nums, target)
        self.assertEqual(result, expected)

    def test_all_zeros(self):
        nums = [0, 0, 0, 0, 0, 0]
        target = 0
        expected = [[0, 0, 0, 0]]
        result = self.solution.fourSum(nums, target)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
