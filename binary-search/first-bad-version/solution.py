"""
you are a product manager and currently leading a team to develop a new
product. Unfortunately, the latest version of your product fails the quality
check. Since each version is developed based on the previous version, all
the versions after a bad version are also bad.

suppose you have n versions [1, 2, ... , n] and you want to find out the
first bad one, which causes all the following ones to be bad.

you are given an API 'bool isBadVersion(version) which returns whether
version is bad. Implement a function to find the first bad version. You
should minimize the number of calls to the API.

example 1:
input: n = 5, bad = 4
result: 4
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

solution: binary search
"""


# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n

        while left < right:
            middle = (left + right) // 2

            # check the left side (case G, G, B, B ,B --> we want to look to the left to find the leftmost bad (the first bad))
            if isBadVersion(middle):
                right = middle
            # check right if we overshot the start of the bads (case G, G, G, G, B)
            else:
                left = middle + 1

        return right
