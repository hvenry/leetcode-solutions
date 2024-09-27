"""
You are given an array of integers stones where stones[i] is the weight of
the i^th stone.

We are playing a game with the stones. On each turn, we choose the heaviest
two stones and smash them together. Suppose the heaviest two stones have
weights x and y with x <= y. The result of the smash is

- If x == y, both stones are destroyed
- If != y, the stone of weight x is destroyed, and the stone of weight
y has weight y - x.

At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left
return 0.

Solution: Simulate the instructions with a MAX heap (we are taking the max stones each iteration)
- to make a min heap, we add negatives to each number

Time complexity: O(n log n)
- log n: get max from heap
- n: get the max n times


"""

from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # put all stones in min heap (python does not have max heap)
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            # (second is smaller since it is negative)
            if second > first:
                # second - first is the weight we want to add
                heapq.heappush(stones, first - second)

        # edge case
        stones.append(0)

        # since stones is negative, we need absolute value
        return abs(stones[0])
