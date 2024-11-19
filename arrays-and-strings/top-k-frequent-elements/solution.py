"""
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example:
nums = [1, 1, 1, 2, 2, 3]
k = 2
returns: [1, 2]

O(n log n) solution :
- use hash map to store frequencies: O(n)
- sort hash map in descending order:  O(n log n)
- return first k numbers

O(n log k) solution (min heap):
- use hash map to store frequencies
- heapify this hashmap (by frequency, log k interactions with heap)
    - O log k interaction to move things in heap
- pop off k largest


Optimal Solution (O(n) answer):
Visualization of regular bucket sort:
nums = [1, 1, 1, 2, 2, 100]
buckets = [0, 3, 2, ... , 1]   <- count
           0, 1, 2, ... , 100] <- index

This does not work, we do want our length of buckets be the largest element of nums.

Visualization of our bucket sort:
nums = [1, 1, 1, 2, 2, 100]
buckets = [[0], [100], [2], [1], [0], [0], [0]] -> values
            0    1      2    3    4    5    6   -> i (count)

Our buckets is limited to n + 1 lenght now.

After constructing buckets that contain elements of that index frequency:
- We then scan backwards from n to get our k elements.
    - scanning backwards will go from highest to lowest frequency
    - scanning forwards will go from lowest to highest frequency

Complexity:
- Time: O(n)
- Space: O(n)
"""

from typing import List
# from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n) Solution -> Bucket sort
        n = len(nums)

        count = {}
        freq = [[] for _ in range(n + 1)]

        # store num in the frequency bucket
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # for every key value pair, we want to append at index count the value
        for num, count in count.items():
            freq[count].append(num)

        res = []

        # go backwards through buckets
        for i in range(len(freq) - 1, 0, -1):
            # we do this because there may be multiple numbers that have the same frequency
            for num in freq[i]:
                res.append(num)

                # return res when we are at k elements
                if len(res) == k:
                    return res

        # O(n log k) solution
        # counter = Counter(nums)
        #
        # heap = []
        #
        # for num, frequency in counter.items():
        #     if len(heap) < k:
        #         heapq.heappush(heap, (frequency, num))
        #     # maintain our sorted by frequency property for k items
        #     else:
        #         heapq.heappushpop(heap, (frequency, num))
        #
        # # return the items in the heap (heaps are just python lists)
        # return [h[1] for h in heap]
