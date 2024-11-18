import unittest
from solution import Solution


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_case_with_negative_numbers(self):
        self.assertEqual(self.solution.twoSum([-3, 4, 3, 90], 0), [0, 2])

    def test_case_with_multiple_solutions(self):
        self.assertEqual(self.solution.twoSum([1, 2, 3, 4, 5], 6), [1, 3])

    def test_case_with_large_numbers(self):
        self.assertEqual(
            self.solution.twoSum([1000000, 500000, -1500000], -1000000), [1, 2]
        )

    def test_case_with_duplicates(self):
        self.assertEqual(self.solution.twoSum([3, 3], 6), [0, 1])

    def test_case_with_no_solution(self):
        self.assertEqual(self.solution.twoSum([1, 2, 3], 7), [])


if __name__ == "__main__":
    unittest.main()
