"""
given a string s, return True if it is a palindrome, or False otherwise

tips
- use .isalnum() to see if left or right pointer char is not a number
- use two pointers to check left and right side of string to see if palindrome
- continue until loop finishes, if it does and no left or right char is different, return True
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
