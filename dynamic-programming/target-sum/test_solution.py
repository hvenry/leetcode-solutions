import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        nums = [1, 1, 1, 1, 1]
        target = 3
        self.assertEqual(self.solution.findTargetSumWays(nums, target), 5)

    def test_single_element(self):
        nums = [1]
        target = 1
        self.assertEqual(self.solution.findTargetSumWays(nums, target), 1)
        target = -1
        self.assertEqual(self.solution.findTargetSumWays(nums, target), 1)

    def test_no_solution(self):
        nums = [1, 2, 3]
        target = 7
        self.assertEqual(self.solution.findTargetSumWays(nums, target), 0)

    def test_all_zeros(self):
        nums = [0, 0, 0, 0, 0]
        target = 0
        self.assertEqual(self.solution.findTargetSumWays(nums, target), 32)


if __name__ == "__main__":
    unittest.main()
