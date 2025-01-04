"""
Given a string s, return the number of unique palindromes of length three that are a
subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still
only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some
characters (can be none) deleted without changing the relative order of the remaining
characters (ie "ace" is a subsequence of "abcde" -> "a_c_e").

Example:
s = "aabca"
returns: 3

- "aba" is a subsequence and is a palindrome
- "aaa" is a subsequence and is a palindrome
- "aca" is a subsequence and is a palindrome
- There are 3 total palindromic subsequences of length 3.

Intuition:
- The O(n^3) approach requires us to use three pointers to find each subsequence, we can
  do the comparisons in in O(1) time since only left and right need to match.
- The O(n^2) approach uses a middle pointer and constructs hashsets of left and right
  charactes every time middle is moved forwards.

Solution:
- Use a set to track the seen left values of the string s.
- Use a hashset to store the count of all the characters in s.
- For each character in s
    - Start with middle at index 0, decrement the counter by the seen character.
    - For all values in left (set) see if there is a match where right also contains
      the character. This checks for a valid palindrome, add to res if True.
    - Once this comparison has terminated, add the seen character to the left set.
- Return the total amount of palindromes in res. Since it is a set, they will be unique.

Complexity:
- Time: O(n)
- Space: O(n)
"""

from collections import Counter


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left = set()
        right = Counter(s)

        for middle in s:
            # remove from right side
            right[middle] -= 1

            # check if palindrome
            for c in left:
                if right[c] > 0:
                    res.add((middle, c))

            # add to left side
            left.add(middle)

        return len(res)
