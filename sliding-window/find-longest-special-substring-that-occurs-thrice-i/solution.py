"""
You are given a string s that consists of lowercase English letters.

A string is called special if it is made up of only a single character. For example, the string "abc" is not special,
wheras the strings "ddd", "zz", and "f" are special.

Return the length of the longest special substring of s which occurs at least thrice, or -1 if no special substring
occurs at least thrice.

Example:
s = "aaaa"

returns: 2
- The longest special substring that occurs three times is "aa", which are "aaxx", "xaax", "xxaa".

Solution:
- we know the max length of special substring can be at most length of the string, so we can can do a binary
  search on these values 1 to n for log n time to locate a valid window size where a frequency is equal to 3.
- for each value, see if the the window is valid by checking if there is a frequency that is at least i

Complexity
- Time: O(n log n) -> iterate through each char in s log n times to find the max value.
- Space: O(n) -> we will need a hashmap to store the frequencies of each iteration
"""

from collections import defaultdict


class Solution:
    def maximumLenght(self, s: str) -> int:
        def is_valid(k: int) -> bool:
            freq = defaultdict(int)
            for i in range(len(s) - k + 1):
                substring = s[i : i + k]
                freq[substring] += 1

                if freq[substring] >= 3:
                    return True

            return False

        left = 1
        right = len(s)
        res = 0

        while left <= right:
            mid = (left + right) // 2

            if is_valid(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1

        return res if res != 0 else -1
