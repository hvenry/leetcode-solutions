from typing import List


# we are looking if a sequence of chars (as a string) s appears inside another string t in the same order
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # no chars in s
        if not s:
            return True

        i = 0
        for char in t:
            # check each char in subsequence
            if s[i] == char:
                i += 1
                # see if length of chars in subsequence has been found
                if i == len(s):
                    return True

        return False
