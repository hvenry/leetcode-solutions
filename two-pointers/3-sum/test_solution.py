import unittest
from solution import Solution


class TestThreeSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, -1, 2], [-1, 0, 1]]
        self.assertEqual(self.solution.threeSum(nums), expected)

    def test_no_triplets(self):
        nums = [1, 2, -2, -1]
        expected = []
        self.assertEqual(self.solution.threeSum(nums), expected)

    def test_all_zeros(self):
        nums = [0, 0, 0, 0]
        expected = [[0, 0, 0]]
        self.assertEqual(self.solution.threeSum(nums), expected)

    def test_multiple_triplets(self):
        nums = [-2, 0, 1, 1, 2]
        expected = [[-2, 0, 2], [-2, 1, 1]]
        self.assertEqual(self.solution.threeSum(nums), expected)


if __name__ == "__main__":
    unittest.main()
