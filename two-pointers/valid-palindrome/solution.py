"""
A prhase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include the letters
and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example:
s = "A man, a pln, a canal: Panama"
returns: True

"amanaplaneacanalpanama" is a palindrome.

Solution:
- use two pointers to check left and right side of string to see if palindrome
- use .isalnum() to see if left or right pointer char is not a number
- continue until loop finishes, if it does and no left or right char is different, return True

Complexity
- Time: O(n)
- Space: O(1)
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
