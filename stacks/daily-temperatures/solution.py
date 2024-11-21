"""
Given an array of integers temperatures, return an array answer such that answer[i] is the number of
days you have to wait after the ith day to get a warmer temperature. If there is no future day, set
answer[i] to 0.

Example:
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
returns: [1, 1, 4, 2, 1, 1, 0, 0]

- for temperatures[0] you need to wait 1 day for a warmer temperature.
- for temperatures[6] there is no day that gets warmer, so 0.

Naive approach:
O(n^2), check each index, and check every index after to see if there is a day that is warmer.

Solution;
- use a monotonic decreasing stack (items are always in decreasing (or equal) order):
- the stack tracks how many times you need to remove a temperature from the to make the current temp higher
    - popping a single item from the stack until it is larger will give us the amount of days until a hotter temp
      is reached.

Visualization [73, 74, 75, 71, 69, 72, 76, 73]:

index 0, temp 73:

res   = [0, 0, 0, 0, 0, 0, 0]
stack = [(73, 0)]


index 1, temp 74:
    since temp > stack -1, we pop from stack, and calculate new index - stack_index (1 - 0 = 1)
    res   = [1, 0, 0, 0, 0, 0, 0, 0]
    stack = [(74, 1)]

index 2, temp 75:
    since temp > stack -1 we pop from stack, and calculate index - stack_index (2 - 1 = 1)

    res   = [1, 1, 0, 0, 0, 0, 0, 0]
    stack = [(75, 2)]

index 3, temp 71:
    res   = [1, 1, 0, 0, 0, 0, 0, 0]
    stack = [(75, 2), (71, 3)]

index 4, temp 69:
    res   = [1, 1, 0, 0, 0, 0, 0, 0]
    stack = [(75, 2), (71, 3), (69, 4)]

index 5, temp 72:
    since temp > stack -1, we pop from stack, and calculate index - stack index (5 - 4 = 1)
    res   = [1, 1, 0, 0, 1, 0, 0, 0]
    stack = [(75, 2), (71, 3)]

    since temp is still > stack - 1, we pop from stack, and calculate index - stack index (5 - 3 = 2)
    res   = [1, 1, 0, 2, 1, 0, 0, 0]
    stack = [(75, 2), (72, 5)]

index 6, temp 76:
    since temp > stack -1, we pop from stack, and calculate index - stack index (6 - 5 = 1)
    res   = [1, 1, 4, 2, 1, 1, 0, 0]
    stack = [(75, 2)]

    since temp > stack -1, we pop from stack, and calculate index - stack index (6 - 2 = 4)
    res   = [1, 1, 4, 2, 1, 1, 0, 0]
    stack = [(76, 6)]

index 7, temp 73:
    res   = [1, 1, 4, 2, 1, 1, 0, 0]
    stack = [(76, 6), (73, 7)]

Nothing left to do, return answer!


Complexity:
- Time: O(n)
- Space: O(n)
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i, temp in enumerate(temperatures):
            # pop from stack until we get a temp that is higher again (maintain monotonic decreasing stack)
            while stack and temp > stack[-1][0]:
                _, stack_i = stack.pop()
                res[stack_i] = i - stack_i

            stack.append((temp, i))

        return res
