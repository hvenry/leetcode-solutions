"""
You are gien a 0-indexed array of integers nums of lenght n. You are initially
positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i.
In other words, if you are at nums[i], you can jump at any nums[i + j], where:
- 0 <= j <= nums[i] and
- i + j < n

Return the minimum number of jumps to reach nums[n - 1].

Difference from Jump Game I:
- This question requires minimum jumps, jump game 1 required a true or false if it
  was possilbe to make the jump (solved with greedy).
- Also, all tests have a solution where jumps are possible.

Example 1:
nums = [2, 3, 1, 1, 4]
returns 2

The minimum number of jumps to reach the last index is 2. You can:
- jump 1 step from index 0 to 1
- jump 3 steps to the last index (1 to 4)

Backtracking Solution:
- check each reachable index for each jump, and then repeat this until the base case is met (we are at end)

Optimal Approach Gredy Solution:
- divide nums into regions that can be reached by x jumps from index 0

    [2, 3, 0, 0, 2, 1, 4]
    <-><----><----><---->
     0   1     2      3

- use i, end and far
    - i         -> the current index
    - end       -> the end of the current region
    - far       -> furthest point we can jump to
    - smallest  -> keep track of how much we need to jump, we add 1 to it when we reach the end of a region

- we increment i and set the new far region value (i + nums[i])
- keep adjusting end, far, smallest until the end of the list has been reached (we always know this is possible)

Solution

index 0:
 [2, 3, 0, 0, 2, 1, 4]
  i     far
  end
 smallest = 1, update end to far
 [2, 3, 0, 0, 2, 1, 4]
  i     far
        end

index 1:
 [2, 3, 0, 0, 2, 1, 4]
     i        far
        end

index 2:
 [2, 3, 0, 0, 2, 1, 4]
        i     far
        end
 smallest = 2
 [2, 3, 0, 0, 2, 1, 4]
        i     far
              end

index 3:
 [2, 3, 0, 0, 2, 1, 4]
           i  far
              end

index 4:
 [2, 3, 0, 0, 2, 1, 4]
              far
              end
              i
 smallest = 3
 [2, 3, 0, 0, 2, 1, 4]
                    far
                    end
              i --> i

If we  follw this, we will se that i can reach the end and the smallest value of 3 is returned.


Complexity:
- Time: O(n)
- Space: O(1)
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        smallest = 0
        n = len(nums)
        end, far = 0, 0

        for i in range(n - 1):
            # furthest we can currently get to
            far = max(far, i + nums[i])

            # we increment smallest when we need to leave a region
            if i == end:
                smallest += 1
                end = far

        return smallest

        # backtracking solution: Not an optimal solution
        # n = len(nums)
        # smallest = float("inf")
        #
        # def backtrack(i=0, jumps=0):
        #     nonlocal smallest
        #
        #     # base case (we are at the end of the array)
        #     if i == n - 1:
        #         smallest = min(smallest, jumps)
        #         return
        #
        #     max_jump = nums[i]
        #
        #     # stay within bounds of the array
        #     max_reachable_index = min(i + max_jump, n - 1)
        #
        #     # start at each reachable index,
        #     for new_index in range(max_reachable_index, i, -1):
        #         backtrack(new_index, jumps + 1)
        #
        # backtrack()
        # return int(smallest)
