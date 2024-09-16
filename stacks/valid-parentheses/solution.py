"""
given a string s containing just the characters '(', ')', '{', '}', '[', ']'
determine if the input string is valid.

valid strings are:
- open brackets must be closed by the same type of brackets
- open brackets must e closed in the correct order
- every close bracket has a corresponding open bracket of the same type

example
s = "()[]{}"
output: true


solution:
- use a stack to track what parentheses needs to be matched next
- use a hashmap to see if the closing parenthesis matches the one that should be closed next
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # match every closing parentheses to correct opening parentheses
        hash_map = {")": "(", "}": "{", "]": "["}

        for char in s:
            # this checks if it is a closing parentheses
            if char in hash_map:
                # if our next up element in the stack is a matching parentheses
                # ie ')' is in hash_map, the value mapped is '(', if '(' s the next last element in the stack, it is closed correctly
                if stack and stack[-1] == hash_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack
