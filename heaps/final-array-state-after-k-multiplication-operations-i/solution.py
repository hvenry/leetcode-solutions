"""
You are given an integer array nums, an integer k, and an integer multiplier.

You need to perform k operations on nums. In each operation:
- Find the minimum value x in nums. If there are multiple occurrences of the minimum value, seelct the one that
  appears first.
- Replace the selected minimum value x with x * multiplier.

Return an integer array denoting the final state of nums after performing k operations.

Example:
nums = [2, 1, 3, 5, 6]
k = 5
multiplier = 2
returns: [8, 4, 6, 5, 6]

Solution:
- Creat a copy of our nums acting as the resulting array to perform operations on
- Heapify our numbers, use a min heap sorted by the value that contains the index of the current number.
- Pop from the heap k times, multiply our resulting array index by 2, add the new value of res*2 which is value to the heap
- return res

Complexity:
- Time: O(n + k log n) -> we perform k operations on the heap in log n time
- Space: O(n)
"""

from typing import List
import heapq


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        res = nums[::]

        h = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(h)

        for _ in range(k):
            _, i = heapq.heappop(h)
            res[i] *= multiplier
            heapq.heappush(h, (res[i], i))

        return res
