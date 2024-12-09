"""
Koko loves to eat bananas. There are n piles of bananas, the i^th pile has piles[i] bananas.
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chosses some pile of bananas and eats k
bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more
bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the banans before the guards return.

Return the maximum integer k such that she can eat all the bananas within h hours.

Example 1:
pils = [3, 6, 7, 11]
h = 8

returns: 4

example:
piles = [30, 11, 23, 4, 20]
h = 5

returns: 30


Solution:
- we are seraching for a k that is in the range of 1 to max value of piles
- we can use a binary search to turn this from O(n) to O(log n)
- for every 'k' value (this is the middle of our binary serach) we calculate to see if we can eat all piles of
  bananas in under h hours.
- this can be found by dividing each pile by the current 'k' value to check if the amount of divisions is less than
  h hours. If it is, then we have found a valid k value (pace) to eat bananas at.
- return the lowest found valid value of k at the end of this binary search

Complexity:
- Time: O(n * log m) -> n piles, m is the max number
- Space: O(1)
"""

from typing import List
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right

        # seraching for a valid k from 1 to max value inpiles.
        while left <= right:
            k = (left + right) // 2
            hours = 0

            for p in piles:
                # rate of eating
                hours += ceil(p / k)

            if hours <= h:
                res = k
                right = k - 1
            else:
                left = k + 1

        return res
