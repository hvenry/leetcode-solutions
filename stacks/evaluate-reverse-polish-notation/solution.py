from typing import List

"""
evaluate the value of an arithmetic expression in reverse polish notation

valid operators: +, -, *, /
each operand may be an integer or another expression

NOTE:
- division between two integers should truncate toward zero
- inputted expression is always valid
- no division by zero error

how does reverse polish notation work?

solution: use a stack
- add each expression value to the stack
- whenever there is an operand that is the current value read, remove top 2 items
from the stack and perform the operation on the two of them. (this is the trick to this question)

time: O(n)
space: O(n) -> for the stack
"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                # order matters, reverse
                # ie: [2, 1, -], the 1 is popped before the 2, but we want 2 - 1, not 1 - 2, so reverse
                x, y = stack.pop(), stack.pop()
                stack.append(y - x)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                # order also matters here
                x, y = stack.pop(), stack.pop()
                stack.append(int(y / x))
            else:
                stack.append(int(token))

        return stack[0]
