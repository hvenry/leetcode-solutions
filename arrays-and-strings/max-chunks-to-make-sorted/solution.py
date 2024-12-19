"""
You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].

We split arr into some number of chunks (ie paritions), and individually srot each chunk. After concatenating them, the
result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.

Example:
arr = [4, 3, 2, 1, 0]

returns: 1
- Splitting into two or more chunks will not return the required result
- For instance, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2] which isn't sorted.

Example 2:
arr = [1, 0, 2, 3, 4]

returns: 4
- We can spit into two chunks, such as [1, 0], [2, 3, 4].
- We can split further into [1, 0], [2], [3], [4]

Solution:
- The max possible number we can have is n, and that is when our inputted list is already sorted
- Noting this, we need to be greedy with our partitions, to try to partition as early and frequently as possible.
- We can only sucessfully partition when our max value is equal to index i
    - for example, [1, 0, 2] cannot be partitioned at index 0, but can be partitioned at index 1 because the max value is 1.
    - this leads to [1, 0, | 2], which can be sorted to [0, 1, 2].

Complexity:
- Time: O(n)
- Space: O(1)
"""

from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        cur_max = -1
        res = 0

        for i, num in enumerate(arr):
            cur_max = max(num, cur_max)

            if cur_max == i:
                res += 1

        return res
