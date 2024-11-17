import unittest
from solution import Solution


class TestConvertToBase7(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_positive_number(self):
        self.assertEqual(self.solution.convertToBase7(100), "202")

    def test_zero(self):
        self.assertEqual(self.solution.convertToBase7(0), "0")

    def test_negative_number(self):
        self.assertEqual(self.solution.convertToBase7(-100), "-202")

    def test_small_positive_number(self):
        self.assertEqual(self.solution.convertToBase7(7), "10")

    def test_small_negative_number(self):
        self.assertEqual(self.solution.convertToBase7(-7), "-10")

    def test_single_digit_positive(self):
        self.assertEqual(self.solution.convertToBase7(6), "6")

    def test_single_digit_negative(self):
        self.assertEqual(self.solution.convertToBase7(-6), "-6")

    def test_large_positive_number(self):
        self.assertEqual(self.solution.convertToBase7(343), "1000")

    def test_large_negative_number(self):
        self.assertEqual(self.solution.convertToBase7(-343), "-1000")


if __name__ == "__main__":
    unittest.main()
