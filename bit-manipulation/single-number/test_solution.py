import unittest
from solution import Solution


class TestSingleNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_number(self):
        self.assertEqual(self.solution.singleNumber([4, 1, 2, 1, 2]), 4)
        self.assertEqual(self.solution.singleNumber([2, 2, 1]), 1)
        self.assertEqual(self.solution.singleNumber([1]), 1)
        self.assertEqual(self.solution.singleNumber([0, 1, 0]), 1)
        self.assertEqual(self.solution.singleNumber([17, 12, 5, 12, 5]), 17)
        self.assertEqual(self.solution.singleNumber([10, 10, 20, 30, 30]), 20)


if __name__ == "__main__":
    unittest.main()
