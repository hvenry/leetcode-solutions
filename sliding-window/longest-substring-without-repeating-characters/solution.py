"""
Given a string s, find the length of the longest substring without repeating
characters.

example:
s = "abcabcbb"
result: 3

Answer is "abc", with the length of 3.

Solution: Sliding window approach
- use left and right pointers to create a window
- slide right over one by one adding to a set of seen characters, until it finds
    a character in the seen set.
- if character has already been seen (is in set), increase left until the window is
    valid, and remove each character left sees from the set.
- compare current window length (Right - Left) + 1, to the max window length.
- return the max window length

KEY: when window is valid (no repeating characters) we move over right, when it
    is invalid, we move over left.

O(n) solution, we check every index once.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0

        seen = set()

        for right in range(len(s)):
            # invalid, trying to add current char to set
            while s[right] in seen:
                seen.remove(s[left])
                # move left until valid
                left += 1

            # once valid window, calculate length
            valid_window_length = (right - left) + 1

            # set longest to the max length
            longest = max(longest, valid_window_length)
            seen.add(s[right])

        return longest
