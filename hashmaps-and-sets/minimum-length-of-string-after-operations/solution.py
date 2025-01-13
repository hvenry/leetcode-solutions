"""
You are given a string s.

You can perform the following process on s any number of times:
- Choose an index i in the string such that there is at least one character to
  the left of index i that is equal to s[i], and at least one character to the
  right that is also equal to s[i].
- Delete the closest character to the left of i that is equal to s[i].
- Delete the closest character to the right of i that is equal to s[i].


Return the minimun length of the final string s that you can achieve.

Example:
s = "abaacbcbb"
returns: 5

- Choose index 2, remove indicies 0 and 3, s = "bacbcbb"
- Choose index 3, remove indicies 0 and 5, s = "acbcb"

Solution:
- Get the count of each character in the string
- Iterate through all counts
    - If the count is even, we add +2 to the result
    - If the count is odd, we add +1 to the result

Complexity:
- Time: O(n)
- Space: O(1) -> since we only need to iterate through 26 characters
"""

from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        res = 0

        for count in Counter(s).values():
            if count % 2 == 1:
                res += 1
            else:
                res += 2

        return res
