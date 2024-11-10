"""
Given an integer array nums, return the length of the longest strictly incresaing subsequence.

Example:
nums = [10, 9, 2, 5, 3, 7, 101, 18]
output = 4

The longest increasing subsequence is [2, 3, 7, 101] which has a leght of 4.

Walk Through Example:

nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]

Create an array of the same lenght, and each index i should have the maximum length increasing subsequence assuming we are ending
in the value of the current index i.

[1, 1, 1, 1, 1, 1, 1, 1, 1]
          i

For example, i which vaule is 7, would be set to 4, because the numbers leading up and including it (1, 2, 6, 7), creates a subsequence
of length 4.

[1, 1, 1, 4, 1, 1, 1, 1, 1]
          i

[1, 1, 1, 1, 1, 1, 1, 1, 1]
We will build this from the bottom up. Let's start at 0.

We do not need to make any changes here, this is the base case 1 = 1.

Next, i = 1, value = 3
[1, 2, 1, 1, 1, 1, 1, 1, 1]

Next, i = 2, value = 6
[1, 2, 3, 1, 1, 1, 1, 1, 1]

Next, i = 3, value = 7
[1, 2, 3, 4, 1, 1, 1, 1, 1]

Next, i = 4, value = 9
[1, 2, 3, 4, 5, 1, 1, 1, 1]

Next, i = 5, value = 4.
    - notice that the value now is less than the previous value
    - we go backwards and see what we can and can't use.
        - we can't use value = 9, value = 7, value = 6
        - we can use value = 3, value = 1
    - therefore this inde value is 3.
[1, 2, 3, 4, 5, 3, 1, 1, 1]

Next, i = 6, value = 10
    - we could use the value of 3 to make this up, but a better subsequence would be using al of the numbers leading up to 9 (index 4)
    - we then set it to 6
[1, 2, 3, 4, 5, 3, 10, 1, 1]

Next, i = 7, value = 5
[1, 2, 3, 4, 5, 3, 10, 4, 1]

Next, i = 8, value = 6
[1, 2, 3, 4, 5, 3, 10, 4, 5]

We then return the MAX of this DP array to get the value.

Solution:
- use a nested for loop i starting at the second position of the dp array, and j starting at the first position.
- we check nums[i] is > nums[j], if this is true, then we take the value of nums[j] and add 1 to it for hte value at nums[i].

[1, 3, 6, 7, 9, 4, 10, 5, 6]
 j  i

[1, x, ...]

since nums[i] > nums[j], we set to value + 1, [1, 2, ...]


- we then move the i one index over, and then do the same process, starting from j at index 0
- we  then move j over again, to see if it's value is less than nums[i], if it is, then we take the value and add 1 to it.

[1, 3, 6, 7, 9, 4, 10, 5, 6]
 j     i

[1, 2, x, ...]


[1, 3, 6, 7, 9, 4, 10, 5, 6]
    j  i

[1, 2, 2, ...]


[1, 3, 6, 7, 9, 4, 10, 5, 6]
       i
       j

[1, 2, 3, ...]

Continue this until the dp array is complete. Then return the max of the array.

Complexity:
- Time: O(n^2)
- Space: O(n)

More OPTIMAL:
- Time: O(n log n)
- Space: O(n)
"""

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Bottom up DP approach
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

        # # n log n space complexity approach (use binary search to store smallest possible neding vaules for increasing subsequences of each length)
        # dp = []
        #
        # for num in nums:
        #     left, right = 0, len(dp)
        #
        #     while left < right:
        #         mid = (left + right) // 2
        #         if dp[mid] < num:
        #             left = mid + 1
        #         else:
        #             right = mid
        #
        #     # if left is equal to the length of dp, append num (num is larger than all elements in dp)
        #     if left == len(dp):
        #         dp.append(num)
        #
        #     # Otherwise, replace dp[left] with num, to maintain smallest possbile end values for subsequences
        #     else:
        #         dp[left] = num
        #
        # # the length of dp is the length of the longest increasing subsequence
        # return len(dp)
