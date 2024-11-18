"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
s = "anagram"
t = "nagram"
returns: True

Example 2:
s = "rat"
t = "car"
returns: False

Solution:
- check base case if lenghts of each string do not equal each other
- use a hashtable
- create a list of length 26, add +1 to the char at i if it appears in s, -1 to the char at i if it appears in t
- if they are anagrams, the counts should all be 0 (meaning that they are balanced)
- return False if any val in count is not equal to 0

Complexity:
- Time: O(n + m)
- Space: O(1) -> you may think the count is O(n) space, but since we always know its length is 26 it is fixed therfore constant
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26  # this is technically constance space

        for i in range(len(s)):
            count[ord(s[i]) - ord("a")] += 1
            count[ord(t[i]) - ord("a")] -= 1

        for val in count:
            if val != 0:
                return False
        return True
