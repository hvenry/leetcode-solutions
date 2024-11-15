import unittest
from solution import Solution


class TestZigzagConversion(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        s = "PAYPALISHIRING"
        numRows = 3
        expected = "PAHNAPLSIIGYIR"
        result = self.solution.convert(s, numRows)
        self.assertEqual(result, expected)

    def test_example2(self):
        s = "PAYPALISHIRING"
        numRows = 4
        expected = "PINALSIGYAHRPI"
        result = self.solution.convert(s, numRows)
        self.assertEqual(result, expected)

    def test_single_row(self):
        s = "PAYPALISHIRING"
        numRows = 1
        expected = "PAYPALISHIRING"
        result = self.solution.convert(s, numRows)
        self.assertEqual(result, expected)

    def test_two_rows(self):
        s = "PAYPALISHIRING"
        numRows = 2
        expected = "PYAIHRNAPLSIIG"
        result = self.solution.convert(s, numRows)
        self.assertEqual(result, expected)

    def test_empty_string(self):
        s = ""
        numRows = 3
        expected = ""
        result = self.solution.convert(s, numRows)
        self.assertEqual(result, expected)

    def test_single_character(self):
        s = "A"
        numRows = 3
        expected = "A"
        result = self.solution.convert(s, numRows)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
