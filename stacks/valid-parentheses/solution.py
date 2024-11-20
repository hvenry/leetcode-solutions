"""
Given a string s containing just the characters '(', ')', '{', '}', '[', ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets
2. Open brackets must e closed in the correct order
3. Every close bracket has a corresponding open bracket of the same type

Example 1:
s = "()[]{}"
returns: true

Exampel 2:
s = (]"
returns: false


Solution:
- Use a stack to track what parentheses needs to be matched next
- Use a hashmap to see if the closing parenthesis matches the one that should be closed next

Complexity:
- Time: O(n) -> we need to go every char to make sure it is matched.
- Space: O(n) -> we can have at most n items in the stack
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
