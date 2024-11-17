import unittest
from solution import Solution


class TestHammingWeight(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_hammingWeight(self):
        self.assertEqual(self.solution.hammingWeight(11), 3)  # 1011
        self.assertEqual(self.solution.hammingWeight(128), 1)  # 10000000
        self.assertEqual(self.solution.hammingWeight(0), 0)  # 0
        self.assertEqual(self.solution.hammingWeight(1), 1)  # 1
        self.assertEqual(self.solution.hammingWeight(255), 8)  # 11111111
        self.assertEqual(self.solution.hammingWeight(1023), 10)  # 1111111111
        self.assertEqual(self.solution.hammingWeight(2147483647), 31)  # 2^31 - 1


if __name__ == "__main__":
    unittest.main()
