"""
Given an integer array nums and an integer k, return the kth largest element in
the array.

Note that it is the kth largest element in the sorted order, not the kth distinct
element.

Can you solve without sorting?

Example 1:
nums = [3, 2, 1, 5, 6, 4]
k = 2

output: 5

Because the kth largest element (2nd largest element) is 5.

Solution: max heap
- Use a max heap to store all numbers O(n)
- pop elements k times (pop in a heap takes O(log n) time

time: O(n + k log n)
- building heap takes O(n)
- each extraction takes O(log n), we do it k times, therefore: k log n


Solution: min heap
Solution using min heap (maintain k items in heap, then pop top element)
This works because if you only have k items in the heap, and it is a min hea,
the heap will contain the K largest elements that we have seen. therefore
heap[0] is our result.

time: O(n log k)
- insertion takes O(log k), doing k elements takes O(k log k)
- remaining (n - k):
    - replacing root takes O log k, and is done n - k times
    therefore: O((n - k) log k)

finally,
O(k log k) + O((n - k) log k) = O( n log k )
"""

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Max heap solution (commented out)
        # # turn min heap to max heap (python does not have max heaps)
        # for i in range(len(nums)):
        #     nums[i] = -nums[i]

        # heapq.heapify(nums)

        # # pop k - 1 largest elements
        # for _ in range(k-1):
        #     heapq.heappop(nums)

        # # return the last popped element as kth largest element
        # return -heapq.heappop(nums)

        # min heap solition
        min_heap = []

        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                heapq.heappushpop(min_heap, num)

        return min_heap[0]
