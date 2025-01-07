import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        self.assertEqual(self.solution.minOperations("110"), [1, 1, 3])

    def test_all_zeros(self):
        self.assertEqual(self.solution.minOperations("000"), [0, 0, 0])

    def test_all_ones(self):
        self.assertEqual(self.solution.minOperations("111"), [3, 2, 3])

    def test_single_one(self):
        self.assertEqual(self.solution.minOperations("100"), [0, 1, 2])
        self.assertEqual(self.solution.minOperations("001"), [2, 1, 0])


if __name__ == "__main__":
    unittest.main()
