"""
You are given an integer array nums. You initially positioned at the array's first index, and each element
in the array represeents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example:
nums = [2, 3, 1, 1 4]
output: True

Jump 1 step (you can jump 1 because it is less than the max of 2) from index 0 to 1, and then jump 3 to 4.


Example 2:
nums [3, 2, 1, 0, 4]
output: False

Returns False because you always get stuck at index 3.

This is easy to code up as a recurrence relation, and we can use a memoization approach to lower out rime comlexity.


Optimal Solution: GREEDY APPROACH
- start at end, and mark as goal.
- we move our goal to the left, checking if at the current index, we can reach the goal from a 1 to max jump

Visualization
[2, 3, 1, 1, 4]
             G  <- initial position of Goal

[2, 3, 1, 1, 4]
          G     <- we move over the goal, since we can jump from 1 to 4.

[2, 3, 1, 1, 4]
       G        <- we move over the goal, since we can jump from 1 to 1.


[2, 3, 1, 1, 4]
    G           <- we move over the goal, since we can jump from 3 to 1.

[2, 3, 1, 1, 4]
 G              <- we move over the goal, since we can jump from 2 to 3.

If goal is at index 0, then it is possible to jump from one end to the other.
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # # Recursive Solution, Time: O(max(nums) ^ n), Space: O(n) -> recursive callstack
        # n = len(nums)
        #
        # def can_reach(i):
        #     # we have reached the end of the list (true)
        #     if i == n - 1:
        #         return True
        #
        #     # for every possible jump, check if the jump leads to the end of the array
        #     for jump in range(1, nums[i] + 1):
        #         if can_reach(i + jump):
        #             return True
        #
        #     return False
        #
        # return can_reach(0)

        # # Top down (memoization) DP approach, Time: O(n^2), space: O(n)
        # n = len(nums)
        # memo = {n - 1: True}
        #
        # def can_reach(i):
        #     if i in memo:
        #         return memo[i]
        #
        #     # try out all jump from 1 to max jump length
        #     for jump in range(1, nums[i] + 1):
        #         if can_reach(i + jump):
        #             memo[i] = True
        #             return True
        #
        #     memo[i] = False
        #     return False
        #
        # return can_reach(0)

        # Greedy approach (starting from the end), Time: O(n), Space: O(1)
        n = len(nums)
        # target is end of the array
        target = n - 1

        # go backwards from n-1 to -1 inclusive (0), and decrement by 1
        for i in range(n - 1, -1, -1):
            max_jump = nums[i]

            # if we can reach the target, then we can get there from the given index
            # THE TARGET IS THE INDEX!! NOT VALUE
            if i + max_jump >= target:
                target = i

        return target == 0
