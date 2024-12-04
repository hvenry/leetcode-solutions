"""
You are given two 0-indexed strings str1 and str2.

In an operation, you select a set of indices in str1, and for each index i in the set, increment str1[i] to the next
character cyclically. That is 'a' becomes 'b', 'b' becomes 'c' and so on, and 'z' becomes 'a'.

Return true if it is possible to make str2 a subsequence of str1 by performing the operation at most once, and false
otherwise.

Example:
str1 = "abc"
str2 = "ad"
returns: true

- Increment str1[2] to become 'd', str1 becomes "abd" and now str2 "ad" is a subsequence of str1.

Solution:
- Iterate through each character in str1, checking if either the char with the cyclical operation or current char equals
  the current index of str2 we are trying to match.
- Keep iterating through each char, updating the index if we find a matching char.
- At the end of the loop we can check if the index lenght is the same as lenght of string2, to see if we matched all chars.

Complexity:
- Time: O(n)
- Space: O(1)
"""


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        index = 0

        for char in str1:
            # calculate next char using cyclical operatoin
            cyclical_char = "a" if char == "z" else chr(ord(char) + 1)

            if index < len(str2):
                if str2[index] in (char, cyclical_char):
                    index += 1

        # True if we have seen all indexes in str2, meaning there is a possible subsequence
        return index == len(str2)
