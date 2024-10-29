import unittest
from solution import Solution


class TestGenerateParenthesis(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_generate_parenthesis_n_1(self):
        self.assertEqual(self.solution.generateParenthesis(1), ["()"])

    def test_generate_parenthesis_n_2(self):
        self.assertEqual(self.solution.generateParenthesis(2), ["(())", "()()"])

    def test_generate_parenthesis_n_3(self):
        self.assertEqual(
            self.solution.generateParenthesis(3),
            ["((()))", "(()())", "(())()", "()(())", "()()()"],
        )

    def test_generate_parenthesis_n_4(self):
        self.assertEqual(
            self.solution.generateParenthesis(4),
            [
                "(((())))",
                "((()()))",
                "((())())",
                "((()))()",
                "(()(()))",
                "(()()())",
                "(()())()",
                "(())(())",
                "(())()()",
                "()((()))",
                "()(()())",
                "()(())()",
                "()()(())",
                "()()()()",
            ],
        )

    def test_generate_parenthesis_n_0(self):
        self.assertEqual(self.solution.generateParenthesis(0), [""])


if __name__ == "__main__":
    unittest.main()
