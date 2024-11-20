"""
You are given a string s consiting of the characters a, b, and c, and a non-negative integer k.
Each minute, you may take either the leftmost character of s, or the rightmost character of s.

Return the minimum number of minutes needed for you to take at least k of each character, or return
-1 if it is not possible to take k of each character.

Example:
s = "aabaaaacaabc
k = 2
returns: 8

This is because you need to take a minimum of 3 characters from the left of s -> [a:2, b:1],
and you need to take a minumum of 5 characters from the right of s -> [a:4, b:2, c:2].

Now there are at least k of each element.

Intuition:
- This is a very interesting question, you may think to use two pointers to solve this, but this is not
  effective because you can't see into the future when deciding which pointer would be optimal to move next.
- You then may think to do backtracking, but the solution is much simplier than that.

Optimal Solution:
- Use a SLIDING WINDOW to find the MAXIMUM WINDOW SIZE, such that there are at least k elements for each character.
- By finding the MAXIMUM WINDOW SIZE that fitst this criteria, you are able to determine the smallest amount of minutes
  it would take to find at least k of each character, which is the solution to this problem.

Complexity
- Time: O(n)
- Space: O(n)
"""


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        count = [0, 0, 0]

        for c in s:
            count[ord(c) - ord("a")] += 1

        if min(count) < k:
            return -1

        res = float("inf")
        left = 0

        for right in range(len(s)):
            count[ord(s[right]) - ord("a")] -= 1

            while min(count) < k:
                # removing char at left
                count[ord(s[left]) - ord("a")] += 1
                left += 1

            res = min(res, len(s) - (right - left + 1))

        return int(res)
