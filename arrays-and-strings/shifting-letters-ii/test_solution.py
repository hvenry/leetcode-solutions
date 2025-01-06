import unittest
from solution import Solution


class TestShiftingLetters(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        s = "abc"
        shifts = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]
        expected = "ace"
        self.assertEqual(self.solution.shiftingLetters(s, shifts), expected)

    def test_single_shift_forward(self):
        s = "xyz"
        shifts = [[0, 2, 1]]
        expected = "yza"
        self.assertEqual(self.solution.shiftingLetters(s, shifts), expected)

    def test_single_shift_backward(self):
        s = "abc"
        shifts = [[0, 2, 0]]
        expected = "zab"
        self.assertEqual(self.solution.shiftingLetters(s, shifts), expected)

    def test_no_shifts(self):
        s = "leetcode"
        shifts = []
        expected = "leetcode"
        self.assertEqual(self.solution.shiftingLetters(s, shifts), expected)

    def test_full_range_shifts(self):
        s = "abcdefghijklmnopqrstuvwxyz"
        shifts = [[0, 25, 1]]
        expected = "bcdefghijklmnopqrstuvwxyza"
        self.assertEqual(self.solution.shiftingLetters(s, shifts), expected)


if __name__ == "__main__":
    unittest.main()
