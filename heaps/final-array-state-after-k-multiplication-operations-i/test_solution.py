import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        nums = [2, 1, 3, 5, 6]
        k = 5
        multiplier = 2
        expected = [8, 4, 6, 5, 6]
        self.assertEqual(self.solution.getFinalState(nums, k, multiplier), expected)

    def test_single_element(self):
        nums = [1]
        k = 3
        multiplier = 3
        expected = [27]
        self.assertEqual(self.solution.getFinalState(nums, k, multiplier), expected)

    def test_large_k(self):
        nums = [1, 2, 3]
        k = 3
        multiplier = 2
        expected = [4, 4, 3]
        self.assertEqual(self.solution.getFinalState(nums, k, multiplier), expected)

    def test_no_operations(self):
        nums = [1, 2, 3]
        k = 0
        multiplier = 2
        expected = [1, 2, 3]
        self.assertEqual(self.solution.getFinalState(nums, k, multiplier), expected)


if __name__ == "__main__":
    unittest.main()
