"""
You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original string
where spaces will be added. Each space should be inserted before the character at the given window.

- For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at indices
  5 and 8 respectively. Thus, we obtain "Enjoy Your Coffee".

Return the modified string after the spaces have been added.

Example:
s = "LeetcodeHelpsMeLearn"
spaces = [8, 13, 15]
returns: "Leetcode Helps Me Learn"

Solution
- Use two pointers, one iterating through the string (i) adding the values to result, and a second iterating through
  spaces (j) checking if i < j to see if we need to append a space to res.
- We iterate through these values while i is smaller than the lenght of s (there are still chars to go) AND j is smaller
  than the lenght of spaces (there are still spaces to add)
- If i is less than the lenght of the string at the end of this loop, we just add the rest to res and return it joined with ""

Complexity:
- Time: O(n + m) -> n is lenght of string, m is lenght of spaces
- Space: O(n + m) -> store the result
"""

from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        i, j = 0, 0
        res = []

        while i < len(s) and j < len(spaces):
            if i < spaces[j]:
                res.append(s[i])
                i += 1

            else:
                res.append(" ")
                j += 1

        if i < len(s):
            res.append(s[i:])

        return "".join(res)
