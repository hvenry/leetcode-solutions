import unittest
from solution import Solution


class TestLastStoneWeight(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        self.assertEqual(self.solution.lastStoneWeight([2, 7, 4, 1, 8, 1]), 1)

    def test_all_stones_destroyed(self):
        self.assertEqual(self.solution.lastStoneWeight([2, 2]), 0)

    def test_single_stone(self):
        self.assertEqual(self.solution.lastStoneWeight([1]), 1)

    def test_no_stones(self):
        self.assertEqual(self.solution.lastStoneWeight([]), 0)

    def test_large_numbers(self):
        self.assertEqual(self.solution.lastStoneWeight([10, 4, 2, 10]), 2)

    def test_multiple_smashes(self):
        self.assertEqual(self.solution.lastStoneWeight([3, 7, 8]), 2)


if __name__ == "__main__":
    unittest.main()
