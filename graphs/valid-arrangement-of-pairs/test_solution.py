import unittest
from solution import Solution


class TestValidArrangement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        pairs = [[5, 1], [4, 5], [11, 9], [9, 4]]
        expected_output = [[11, 9], [9, 4], [4, 5], [5, 1]]
        self.assertEqual(self.solution.validArrangement(pairs), expected_output)

    def test_single_pair(self):
        pairs = [[1, 2]]
        expected_output = [[1, 2]]
        self.assertEqual(self.solution.validArrangement(pairs), expected_output)

    def test_two_pairs(self):
        pairs = [[1, 2], [2, 3]]
        expected_output = [[1, 2], [2, 3]]
        self.assertEqual(self.solution.validArrangement(pairs), expected_output)

    def test_multiple_pairs(self):
        pairs = [[1, 3], [3, 2], [2, 1]]
        expected_output = [[1, 3], [3, 2], [2, 1]]
        self.assertEqual(self.solution.validArrangement(pairs), expected_output)

    def test_disconnected_pairs(self):
        pairs = [[1, 2], [3, 4], [2, 3]]
        expected_output = [[1, 2], [2, 3], [3, 4]]
        self.assertEqual(self.solution.validArrangement(pairs), expected_output)


if __name__ == "__main__":
    unittest.main()
