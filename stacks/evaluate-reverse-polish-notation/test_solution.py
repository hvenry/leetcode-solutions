import unittest
from solution import Solution


class TestEvalRPN(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        tokens = ["2", "1", "+", "3", "*"]
        self.assertEqual(self.solution.evalRPN(tokens), 9)

    def test_single_number(self):
        tokens = ["4"]
        self.assertEqual(self.solution.evalRPN(tokens), 4)

    def test_addition(self):
        tokens = ["4", "13", "5", "/", "+"]
        self.assertEqual(self.solution.evalRPN(tokens), 6)

    def test_subtraction(self):
        tokens = ["10", "6", "-"]
        self.assertEqual(self.solution.evalRPN(tokens), 4)

    def test_multiplication(self):
        tokens = ["2", "3", "*"]
        self.assertEqual(self.solution.evalRPN(tokens), 6)

    def test_division(self):
        tokens = ["8", "3", "/"]
        self.assertEqual(self.solution.evalRPN(tokens), 2)

    def test_complex_expression(self):
        tokens = ["4", "13", "5", "/", "+", "2", "*"]
        self.assertEqual(self.solution.evalRPN(tokens), 12)

    def test_negative_numbers(self):
        tokens = ["-2", "3", "*"]
        self.assertEqual(self.solution.evalRPN(tokens), -6)

    def test_mixed_operations(self):
        tokens = ["5", "1", "2", "+", "4", "*", "+", "3", "-"]
        self.assertEqual(self.solution.evalRPN(tokens), 14)


if __name__ == "__main__":
    unittest.main()
