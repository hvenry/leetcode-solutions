"""
Ypu are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:
- Choose the pile with the maximum number of gifts.
- If there is more than one pile with the maximum gifts, choose any.
- Leave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.

Return the number of gifts remaining after k seconds.

Example:
gifts = [25, 64, 9, 4, 100]
k = 4

returns: 29
- k = 1: [25, 64, 9, 4, 10]
- k = 2: [25, 8, 9, 4, 10]
- k = 3: [5, 8, 9, 4, 10]
- k = 4: [5, 8, 9, 4, 3] -> the root of 10 is 3.16 and we take the floor of this.

Solution:
- use a max heap
- perform the operation k times using heapreplace
- return sum of the heap

Complexity:
- Time: O(n + k log n) -> heapify takes O(n) + k heap operations that take log n time
- Space: O(n)
"""

from heapq import heapify, heapreplace
from math import sqrt
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # python uses min_heap for default, we need to negate all our gifts and math ops
        min_heap = [-gift for gift in gifts]
        heapify(min_heap)

        for _ in range(k):
            heapreplace(min_heap, -int(sqrt(-min_heap[0])))

        return -sum(min_heap)
