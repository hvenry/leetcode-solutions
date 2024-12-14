"""
You are given a 0-indexed integer array nums. A subarray of nums is called continuous if:

- Let i, i + i, ... j be the indicies in the subarray. Then, for each pair of indicies,
  i <= i_1, i_2 <= j, 0 <= | nums[i_1] - nums[i_2] | <= 2
  (fancy way of saying abs difference of values need to be 2 or less to be continuous)

Return the total number of continuous subarrays.

A subarray is contiguous non-empty sequence of elements within an array.

Example:
nums = [5, 4, 2, 4]
returns: 8

- Continuous subarray of size 1: [5], [4], [2], [4].
- Continuous subarray of size 2: [5, 4], [4, 2], [2, 4].
- Continuous subarray of size 3: [4, 2, 4]
- No continuous subarrays of size 4. Total = 4 + 3 + 1 = 8


Solution:
- We can use a sliding window approach with a min and max queue of seen values to validate our current window.
- For every window, we maintain our minq and maxq for the new rightmost value added.
- To validate our left side, we can check the difference of our maxq - min1 to see if it violates our <= 2 condition.
- Once this is validated, our res is incremented by the size of the current widow, this keeps track the total sum of all valid subarrays.


Complexity:
- Time: O(n)
- Space: O(n)
"""

from typing import List
from collections import deque


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        minq = deque()
        maxq = deque()

        left = 0
        res = 0

        for right in range(n):
            # vaidate minq
            while minq and nums[minq[-1]] >= nums[right]:
                minq.pop()
            minq.append(right)

            # validate maxq
            while maxq and nums[maxq[-1]] <= nums[right]:
                maxq.pop()
            maxq.append(right)

            # validate window
            while nums[maxq[0]] - nums[minq[0]] > 2:
                left += 1
                if minq[0] < left:
                    minq.popleft()
                if maxq[0] < left:
                    maxq.popleft()

            # add combinations (window length) to our total
            res += right - left + 1

        return res
