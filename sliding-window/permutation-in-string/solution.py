"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1,
or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Permutation: A permutation is a rearrangement of all the characters of a string.

example 1:
s1 = "ab"
s2 = "eidbaooo"
Returns True

s2 contains one permutation of s1 ("ba").

example 2:
s1 = "ab"
s2 = "eidboaoo"
Returns False

Solution: Fixed size sliding window algorithm
- create frequency arrays for the length of s1
- you can also construct s2 frequency for length s1 to save time
- next, use a fixed sliding window of lenght s1, and move it from the lenght of s1 to the length of s1
- every time you move it, update the frequency of s2 string, by adding +1 to the new char seen and -1 to the character that is leaving the window.
- compare the frequencies of both arrays, if they are the same, return True
- if the window completes sliding across the lenght of string, return False
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        s1_counts = [0] * 26
        s2_counts = [0] * 26

        # base case
        if n1 > n2:
            return False

        for i in range(n1):
            s1_counts[ord(s1[i]) - 97] += 1
            s2_counts[ord(s2[i]) - 97] += 1

        # see if they are the same permutation
        if s1_counts == s2_counts:
            return True

        # start inclusive at index of n1
        for i in range(n1, n2):
            # adjust frequency based on the front of the window moving forward
            s2_counts[ord(s2[i]) - 97] += 1
            # adjust frequency based on the back of the window moving forward
            s2_counts[ord(s2[i - n1]) - 97] -= 1

            # see if s1 is the same as s2
            if s1_counts == s2_counts:
                return True

        return False
