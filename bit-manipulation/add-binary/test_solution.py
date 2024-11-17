import unittest
from solution import Solution


class TestAddBinary(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_add_binary(self):
        self.assertEqual(self.solution.addBinary("11", "1"), "100")
        self.assertEqual(self.solution.addBinary("1010", "1011"), "10101")
        self.assertEqual(self.solution.addBinary("0", "0"), "0")
        self.assertEqual(self.solution.addBinary("1111", "1111"), "11110")
        self.assertEqual(self.solution.addBinary("110010", "10111"), "1001001")
        self.assertEqual(self.solution.addBinary("1", "111"), "1000")
        self.assertEqual(self.solution.addBinary("0", "1111"), "1111")
        self.assertEqual(self.solution.addBinary("111", "111"), "1110")


if __name__ == "__main__":
    unittest.main()
