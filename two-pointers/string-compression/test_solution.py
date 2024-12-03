import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        chars = ["a", "a", "b", "b", "c", "c", "c"]
        expected_length = 6
        expected_chars = ["a", "2", "b", "2", "c", "3"]
        length = self.solution.compress(chars)
        self.assertEqual(length, expected_length)
        self.assertEqual(chars[:length], expected_chars)

    def test_example2(self):
        chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        expected_length = 4
        expected_chars = ["a", "b", "1", "2"]
        length = self.solution.compress(chars)
        self.assertEqual(length, expected_length)
        self.assertEqual(chars[:length], expected_chars)

    def test_single_char(self):
        chars = ["a"]
        expected_length = 1
        expected_chars = ["a"]
        length = self.solution.compress(chars)
        self.assertEqual(length, expected_length)
        self.assertEqual(chars[:length], expected_chars)

    def test_no_repeats(self):
        chars = ["a", "b", "c"]
        expected_length = 3
        expected_chars = ["a", "b", "c"]
        length = self.solution.compress(chars)
        self.assertEqual(length, expected_length)
        self.assertEqual(chars[:length], expected_chars)

    def test_long_repeats(self):
        chars = ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]
        expected_length = 3
        expected_chars = ["a", "1", "1"]
        length = self.solution.compress(chars)
        self.assertEqual(length, expected_length)
        self.assertEqual(chars[:length], expected_chars)


if __name__ == "__main__":
    unittest.main()
