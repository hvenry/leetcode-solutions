"""
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

output is three because we have 3 jewels in our string of stones, (a, A, A)
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # O(n + m)
        s = set(jewels)
        count = 0
        for stone in stones:
            # check if our stone is in our set O(1)
            if stone in s:
                count += 1

        # the count is the total jewels we have tracked in our stones
        return count


# Time Complexity: O(n + m)
# Space Complexity: O(n)
