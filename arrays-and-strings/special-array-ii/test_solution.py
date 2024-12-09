import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        nums = [3, 4, 1, 2, 6]
        queries = [[0, 4]]
        expected = [False]
        self.assertEqual(self.solution.isArraySpecial(nums, queries), expected)

    def test_all_odd_numbers(self):
        nums = [1, 3, 5, 7, 9]
        queries = [[0, 4], [1, 3]]
        expected = [False, False]
        self.assertEqual(self.solution.isArraySpecial(nums, queries), expected)

    def test_all_even_numbers(self):
        nums = [2, 4, 6, 8, 10]
        queries = [[0, 4], [1, 3]]
        expected = [False, False]
        self.assertEqual(self.solution.isArraySpecial(nums, queries), expected)

    def test_alternating_parity(self):
        nums = [1, 2, 3, 4, 5, 6]
        queries = [[0, 5], [1, 4], [2, 3]]
        expected = [True, True, True]
        self.assertEqual(self.solution.isArraySpecial(nums, queries), expected)

    def test_two_elements(self):
        nums = [1, 2]
        queries = [[0, 1]]
        expected = [True]
        self.assertEqual(self.solution.isArraySpecial(nums, queries), expected)


if __name__ == "__main__":
    unittest.main()
