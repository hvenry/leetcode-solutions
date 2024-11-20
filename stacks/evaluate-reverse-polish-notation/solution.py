"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note Note that:
- Valid operators are +, -, *, and /.
- Each operand may be an integer or another expression.
- The division between two integers always truncates towards zero.
- There will not be any divions by zero.
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all the intermediate calculations can be represented in a 32-bit integer.

Reverse Polish Notation:
- A mathematical notation in which operators follow their operands.
- Take the operand that is to the left of two numbers, and perform the operation on the both of them ["2", "1", "+"] -> 2 + 1

Example:
tokens = ["2", "1", "+", "3", "*"]
returns: 9

This notation works out to ((2 + 1) * 3) = 9.

Solution:
- Add each expression value to the stack
- Whenever there is an operand that is the current value read, remove top 2 items from the stack and perform the operation on the
  two of them.

Complexity:
Time: O(n) -> iterate through tokens
Space: O(n) -> store at most n tokens in the stack
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                # order matters for subtraction, we need to reverse reverse
                x, y = stack.pop(), stack.pop()
                stack.append(y - x)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                # order matters for multiplication
                x, y = stack.pop(), stack.pop()
                stack.append(int(y / x))
            else:
                stack.append(int(token))

        return stack[0]
