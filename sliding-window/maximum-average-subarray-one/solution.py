"""
You are given an integer array `nums` consisting of `n` elements, and an integer `k`.

Find a contiguous subarray whose length is equal to `k` that has the maximum average
value and return this value. Any answe with a calculation error less than 10^-5 will
be accepted.

example:
nums = [1, 12, -5, -6, 50, 3]
k = 4
maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 5 = 12.75


solution: use a fixed length sliding window (of length k)

- keep track of max average (starts at -inf)
- track current sum = 0


create current sum
- increase current sum, and build the window (by sliding it), adding numbers to the sum until length k
- once window reaches length k, take current sum (sum of all contents of sliding window)
    then divide by k, to get the average of that window.
- compare the result to max_avg, take the lowest of the two values

keep adding and subtracting from current sum (based on window)
- add the next number, and subtract the last number (to maintain our k numbers) from the current sum.
- calculate the average of that window and compare to max average

do this until window has slid across all list items
- return max average

time:
O(n)
"""

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        cur_sum = 0

        # build up the first window
        for i in range(k):
            cur_sum += nums[i]

        max_avg = cur_sum / k

        # iterate through the rest of the list
        for i in range(k, n):
            # calculate sum of current window
            cur_sum += nums[i]
            cur_sum -= nums[i - k]

            avg = cur_sum / k
            max_avg = max(max_avg, avg)

        return max_avg
