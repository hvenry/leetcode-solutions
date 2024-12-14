import unittest
from solution import Solution


class TestContinuousSubarrays(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        nums = [5, 4, 2, 4]
        expected = 8
        result = self.solution.continuousSubarrays(nums)
        self.assertEqual(result, expected)

    def test_single_element(self):
        nums = [1]
        expected = 1
        result = self.solution.continuousSubarrays(nums)
        self.assertEqual(result, expected)

    def test_all_elements_same(self):
        nums = [2, 2, 2, 2]
        expected = 10
        result = self.solution.continuousSubarrays(nums)
        self.assertEqual(result, expected)

    def test_no_continuous_subarrays(self):
        nums = [1, 4, 7]
        expected = 3
        result = self.solution.continuousSubarrays(nums)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
