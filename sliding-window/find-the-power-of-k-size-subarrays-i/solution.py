"""
You are given an array of integers nums of length n and a positive integer k.

The power of an array is defined as:
- Its maximum element of all its elements are consecutive and sorted in ascending order
- -1 otherwise

You need to find the power of all subarrays of nums of size k.

Return an integer array results of size n-k+1, where results[i] is the power of nums[i..(i + k -1)]

Example:
nums = [1, 2, 3, 4, 3, 2, 5], k = 3
returns: [3, 4, -1, -1, -1]

[1, 2, 3] -> append 3, 3 is the max, elements are consecutive and sorted in ascending order
[2, 3, 4] -> append 4, 4 is the max, elements are consecutive and sorted in ascending order
[3, 4, 3] -> append -1, elements are not consecutive
[4, 3, 2] -> append -1, elements are not sorted
[3, 2, 5] -> append -1, elements are not consecutive

Solution
- use a sliding window to construct windows of lenght k
- keep track of a count that is at minimum 1 and at maximum k, which determines if the window is consecutive and ascending
- if the count at an end of the window is equal to k, it means that the elements are in ascending order and are consecutive

How do we maintain this count?
- we check if the next element is the current element + 1 to maintain the property of the elements being consecutive
- after sliding the window from the left, we check if the element we are losing was consecutive, and we subtract one from the count
  if this is true to maintain a maximum of k consecutive elements

Time Complexity:
- Time: O(n)
- Space: O(1)
"""

from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        left = 0

        consecutive_count = 1

        for right in range(n):
            # check if our right pointer is consecutive
            if right > 0 and nums[right - 1] + 1 == nums[right]:
                consecutive_count += 1

            # check if the lenght of the window is bigger than k, to see if we increment our left pointer
            if right - left + 1 > k:
                # check if we are removing a consecutive element to maintain the amount of consecutive elements seen
                if nums[left] + 1 == nums[left + 1]:
                    consecutive_count -= 1

                left += 1

            # now we check if our k length window has k consecutive numbers, if it does we add the rightmost number, if not add -1
            if right - left + 1 == k:
                if consecutive_count == k:
                    res.append(nums[right])
                else:
                    res.append(-1)

        return res
