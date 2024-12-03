import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        s = "LeetcodeHelpsMeLearn"
        spaces = [8, 13, 15]
        expected = "Leetcode Helps Me Learn"
        self.assertEqual(self.solution.addSpaces(s, spaces), expected)

    def test_no_spaces(self):
        s = "HelloWorld"
        spaces = []
        expected = "HelloWorld"
        self.assertEqual(self.solution.addSpaces(s, spaces), expected)

    def test_spaces_at_start(self):
        s = "HelloWorld"
        spaces = [0, 1, 2]
        expected = " H e lloWorld"
        self.assertEqual(self.solution.addSpaces(s, spaces), expected)

    def test_multiple_spaces(self):
        s = "EnjoyYourCoffee"
        spaces = [5, 9]
        expected = "Enjoy Your Coffee"
        self.assertEqual(self.solution.addSpaces(s, spaces), expected)

    def test_consecutive_spaces(self):
        s = "abcdef"
        spaces = [1, 2, 3, 4, 5]
        expected = "a b c d e f"
        self.assertEqual(self.solution.addSpaces(s, spaces), expected)


if __name__ == "__main__":
    unittest.main()
