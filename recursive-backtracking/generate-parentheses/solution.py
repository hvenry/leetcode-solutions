"""
Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

Example 1:
n = 3
Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

Example 2:
n = 1
Output: ["()"]


Solution Explanation:
Start with nothing ' . ':

                    .
        (                       ) <- not valid path

We always go left, so start at ' ( ':

                    (
        ((                      ()
    (((     (()             ()(     ()) <- bad violates rule 1
((()     (()(   (())    ()((    ()()
((())    (()()  (())(   ()(()   ()()(
((()))   (()()) (())()  ()(())  ()()() = our valid solutions

Keep track of how many open and how many closed brackets at any step.

    open:
    close:

Rules:
1. To go down a right path, the condition open > close needs to be true. (we cannot close without open)
2. We also need to keep opening if open < n

Finally, we have a VALID SOLUTION when len(sol) = 2n and it does not break any of our rules.
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, sol = [], []

        def backtrack(open_parentheses, closed_parentheses):
            if len(sol) == 2 * n:
                res.append("".join(sol))
                return

            # left path: use a open parentheses, if open > n
            if open_parentheses < n:
                sol.append("(")
                backtrack(open_parentheses + 1, closed_parentheses)
                sol.pop()

            # right path: use a close parentheses, if open > close
            if open_parentheses > closed_parentheses:
                sol.append(")")
                backtrack(open_parentheses, closed_parentheses + 1)
                sol.pop()

        backtrack(0, 0)
        return res
