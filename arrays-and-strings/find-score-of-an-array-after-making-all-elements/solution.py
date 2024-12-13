"""
You are given an array nums consisting of positive integers.

Starting with score = 0, apply the following algorithm:
- Chose the smallest integer of the array that is not marked.
  If there is a tie, choose the one with the smallest index.
- Add the value of the chosen integer to score.
- Repeat until all the array elements are marked.

Return the score you get after applying the above algorihtm.

Example:
nums = [2, 1, 3, 4, 5, 2]
returns: 7

- we mark 1 and adjacent: [x2, x1, x3,  4,  5,  2] score = 1
- we mark 2 and adjacent: [x2, x1, x3,  4,  5, x2] score = 3
- we amrk 4 and adjacent: [x2, x1, x3, x4, x5, x2] score = 7

Solution:
- Sort the numbers as tuples that also contain the index of them
- Create a set of seen indexes for O(1) lookup
- For every num, index in sorted, we check if it has been seen, if not we add its index and adjacent to seen and add its value to score.

Complexity:
- Time: O(n log n)
- Space: O(n)
"""

from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        seen = set()
        values = [(num, i) for i, num in enumerate(nums)]

        for num, i in sorted(values):
            if i in seen:
                continue

            seen.add(i - 1)
            seen.add(i + 1)
            seen.add(i)
            score += num

        return score
