"""
Given an integer array nums and an integer k, return the length of the shortest non-empty
subarray of nums with a sum of at least k. If there is no such subarray, return -1.

Example:
nums = [2, -1, 2]
k = 3
returns: 3

This question is very similar to minimum-size-subarray-sum, but this time there are negative values, how do we account
for this using a sliding window approach? We use a monotonic deque (intuition leads us to use a stack, but for O(1) operations we use a deque).

Solution
- Key: monotonic increasing order deque that stores prefix sums and index
- Use a sliding window to look for the smallest window, leveraging the deque's ability to remove smallest prefix sums to check if we are still larger than k
    - we return the value

Visualization:
nums = [-1, 2, -1, 2, 3]
k = 3

index 0:
cur_sum = -1
deque = (-1, 0)

index 1:
cur_sum = 1
deque = (-1, 0), (1, 1)

index 2:
cur_sum = 0
                 remove (because this breaks the property of monotonic increasting)
deque = (-1, 0), (1, 1), (0, 2)

index 3:
cur_sum = 2

what can we do to make the sum valid? we can remove the leftmost element of the deque!
        remove
deque = (-1, 0), (0, 2)

now cur_sum = 3 (2 - (-1))
deque = (0, 2), (2, 3)

index 4:
cur_sum = 5 (3 + 2)

        remove (5 - 0 is still greater than k)
deque = (0, 2), (2, 3)
                remove (5 - 2 is still greater than k)

now our smallest possible window is 1 (which is just the 3 at the end)
- return 1.

Complexity:
- Time: O(n)
- Space: O(n)
"""

from typing import List
from collections import deque


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res = float("inf")
        cur_sum = 0
        q = deque()  # store (prefix sum, end index)

        for right in range(len(nums)):
            cur_sum += nums[right]

            # minize our result
            if cur_sum >= k:
                res = min(res, right + 1)

            # find minimum valid window ending at right by checking current sum - prefix sum is greater than k
            # this is where we leverage the monotonic deque
            # the left side of the deque contains our minimum prefix
            while q and cur_sum - q[0][0] >= k:
                _, end_index = q.popleft()
                res = min(res, right - end_index)

            # make sure deque is in monotonic order
            # remove the right most values of the deque if they are larger than cur_sum
            while q and q[-1][0] >= cur_sum:
                q.pop()

            # append the new tuple now that we know our deque is in monotonic order
            q.append((cur_sum, right))

        return -1 if res == float("inf") else int(res)
