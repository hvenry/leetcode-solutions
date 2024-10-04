"""
Koko loves to eat bananas. There are n piles of bananas, the i^th pile has
piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she
chosses some pile of bananas and eats k bananas from that pile. If the pile
has less than k bananas, she eats all of them instead and will not eat any more
bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the banans before
the guards return.

Return the maximum integer k such that she can eat all the bananas within h hours.

example 1:
pils = [3, 6, 7, 11]
h = 8

Output = 4

example 2:
piles = [30, 11, 23, 4, 20]
h = 5

Output = 30


Solution:
k = how many bananas to eat per hour, such that it is the smallest number to eat all bananas in h hours

to start: we can calculate the hours per pile by doing piles[i] / k

we know that the biggestg value of k is also the max(piles)

so k is from [1 to max(piles)]

Since k-max(piles) is ordered, we can use BINARY SEARCH to see if the k is a valid solution for our pile.
- once we have closed in to a value (which will be the minimum value when left = right and no other options exist, return either left or right)
"""

from typing import List
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_works(k):
            hours = 0

            for p in piles:
                # round up, if hours = 3.5, we need 4 hours, if hours is 3.1, we still need 4 hours.
                hours += ceil(p / k)

            return hours <= h

        # implement binary search
        left = 1
        right = max(piles)

        while left < right:
            # k is the same as middle
            k = (left + right) // 2

            # we want to converge to the smallest k value that works
            if k_works(k):
                right = k
            else:
                # we increase by 1 because middle value did not work
                left = k + 1

        # once we have closed into a particular value left will equal right (left < right not true), so we can return either
        return left
