import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        nums = [10, 4, -8, 7]
        self.assertEqual(self.solution.waysToSplitArray(nums), 2)

    def test_example_case_2(self):
        nums = [2, 3, 1, 0]
        self.assertEqual(self.solution.waysToSplitArray(nums), 2)

    def test_single_element(self):
        nums = [1]
        self.assertEqual(self.solution.waysToSplitArray(nums), 0)

    def test_large_numbers(self):
        nums = [1000000000, 1000000000, 1000000000, 1000000000]
        self.assertEqual(self.solution.waysToSplitArray(nums), 2)


if __name__ == "__main__":
    unittest.main()
