"""
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

example 1:
nums = [1, 1, 1, 2, 2, 3]
k = 2

output: [1, 2]

example 2:
nums = [1], k = 1

output: [1]


O(n log n) solution :
- use hash map to store frequencies: O(n)
- sort hash map in descending order:  O(n log n)
- return first k numbers

O(n log k) solution (min heap):
- O log k interaction to move things in heap

- use hash map to store frequencies
- heapify this hashmap (by frequency, log k interactions with heap)
- pop off


O(n) answer:
- there is no way an number can appear more than n times
- min number 0 times, max number 9 times, make array where frequency is index of array
- store the frequency of each given number at the bucket[frequency] (each element in list bucket is a list)
- now, from right to left our buckets contain the most frequent items, we can simply create a list that is k long and return it (from left to right)
"""

from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # #   O(n log k) solution
        #      counter = Counter(nums)

        #     heap = []

        #     for num, frequency in counter.items():
        #         if len(heap) < k:
        #             heapq.heappush(heap, (frequency, num))
        #         # maintain our sorted by frequency property for k items
        #         else:
        #             heapq.heappushpop(heap, (frequency, num))

        #    # return the items in the heap (heaps are just python lists)
        #     return [h[1] for h in heap]

        # O(n) solution
        n = len(nums)
        counter = Counter(nums)

        buckets = [0] * (n + 1)

        # store num in the frequency bucket
        for num, frequency in counter.items():
            # this if else is done to make sure 0 is not left in the bucket
            if buckets[frequency] == 0:
                buckets[frequency] = [num]
            else:
                buckets[frequency].append(num)

        res = []

        # return
        for i in range(n, -1, -1):
            if buckets[i] != 0:
                res.extend(buckets[i])
            # if we have appended k things, then break and return res
            if len(res) == k:
                break

        return res
