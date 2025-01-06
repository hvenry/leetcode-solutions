"""
You are given a string of s lowercase English letters and a 2D integer array shifts
where shifts[i] = [start_i, end_i, direction_i]. For every i, shift the characters in s
from the index start_i to the index end_i (inclusive) forward if direction_i = 1, or
shift the characters backward if direction_i = 0.

Shifting a character forward means replacing it with the next letter in the alphabet
(wrapping around s that 'z' becomes 'a'). Similarly, shifting a character backward means
replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').

Return the final string after such shifts to s are applied.

Example:
s = "abc"
shifts = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]

returns: "ace"

- shifts[0], we shift [0 - 1] "ab" backward to "za", now s = "zac"
- shifts[1], we shift [1 - 2] "ac" forward to "bd", now s = "zbd"
- shifts[2], we shift [0 - 2] "zbd" forward to "ace", now s = "ace"

Brute force:
- This has quadratic time complexity, since we need to iterate over substrings of s
- for each shift in shifts, iterate through range of s either incrementing or
  decrementing s[i] based on shift[2].

Optimal Solution:
- Instead of iterating over s multiple times, we can calculate the total shift amount
  for each character in s using a prefix sum calculated from a difference array.
- We can see how many shifts to apply to each character by comparing it to the previous
  one (prefix sum)
    - This allows us to update runs by using the start and end only, and not having to
      worry about every number inbetween.

Complexity:
- Time: O(n + m) -> O(m) for diff_array, O(n) for the resulting string
- Space: O(n)
"""

from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff_array = [0] * n

        # construct diff array using prefix sum
        for shift in shifts:
            # shifting forward
            if shift[2] == 1:
                diff_array[shift[0]] += 1

                # flag the end of the sequence with a negative
                if shift[1] + 1 < n:
                    diff_array[shift[1] + 1] -= 1

            # shifting backward
            if shift[2] == 0:
                diff_array[shift[0]] -= 1

                # flag the end of the sequence with a positive
                if shift[1] + 1 < n:
                    diff_array[shift[1] + 1] += 1

        res = list(s)
        shift_amount = 0

        # shift characters in s
        for i in range(n):
            # update shift amount based on previous shift amount + diff_array
            shift_amount = (shift_amount + diff_array[i]) % 26

            # normalize shift amount
            if shift_amount < 0:
                shift_amount += 26

            # calculate new shifted character
            shifted_char = chr((ord(s[i]) - ord("a") + shift_amount) % 26 + ord("a"))
            res[i] = shifted_char

        return "".join(res)

    def shiftingLettersBrute(self, s: str, shifts: List[List[int]]) -> str:
        s = list(s)

        # process each shift
        for shift in shifts:
            # forwards
            if shift[2] == 1:
                for i in range(shift[0], shift[1] + 1):
                    s[i] = chr((ord(s[i]) - ord("a") + 1) % 26 + ord("a"))
            # backwards
            if shift[2] == 0:
                for i in range(shift[0], shift[1] + 1):
                    s[i] = chr((ord(s[i]) - ord("a") - 1) % 26 + ord("a"))

        return "".join(s)
