"""
You you are given an integer array nums where the ith bag contains nums[i] balls. You are also given an integer
maxOperations.

You can perform the following operation at most maxOperations times:

- Take a bag of balls and divide it into two new bags with a postiive number of balls.
    - For example, a bag of 5 balls can become two new bags of 1 and r balls, or two new bags of 2 and 3 balls.

Your penalty is the maximum number of balls in a bag. You want to minimize your penalty after the operations.

Example 1:
nums = [9]
maxOperations = 2
returns: 3

- Divide [9] into [6, 3]
- Divide [6, 3] ino [3, 3, 3]
- Return 3, this is the max value

Solution:
- We can calculate the required operations to get values from 1 to n (max_balls).
    - When we calculate the required operations, we can return True if it is possible to do it under maxOperations
    - Doing this, we can determine which value from 1 to n is the highest value we can achieve using maxOperations
        - We can find this value in log(m) time using binary search

- To calculate maxOperations for a single value of balls:
    - n / max_balls, then round up to get a whole number of operations
    - subtract 1 from this to account for starting value

Example Calculation:
    n = 9, max_balls = 3
    (9 / 3) - 1 = 2 --> operations to get this max_balls value, which is correct because [9] = [3] [3] [3] with 2 operations.


Complexity:
- Time: O(n * log(m)) -> O(n * m) without binary search optimization
- Space: O(1)
"""

from typing import List
from math import ceil


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # helper function to find the max operations
        def can_divide(max_balls):
            operations = 0

            # we see if all numbers can be validated WHILE STAYING BELOW operations
            for n in nums:
                # We round up the total number of operations (n / max_balls), -1 to account for original number
                operations += ceil(n / max_balls) - 1

                if operations > maxOperations:
                    # we went above operations, return False
                    return False

            return True

        left = 1
        right = max(nums)

        # binary search, we check numbers 1 to n to see if they can be achieved without exceeding maxOperations
        while left < right:
            middle = (left + right) // 2

            if can_divide(middle):
                right = middle
            else:
                left = middle + 1

        return left
