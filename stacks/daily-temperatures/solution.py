from typing import List

"""
given an array of integers 'temperatures', return an array 'answer'
such that answer[i] is the number of days you have to wait after the ith day
to get a warmer temperature.

if there is no future day, set answer[i] to 0.

example:
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
result: [1, 1, 4, 2, 1, 1, 0, 0]

for temperatures[0] you need to wait 1 day for a warmer temperature.
for temperatures[6] there is no day that gets warmer, so 0.

naive approach: O(n^2), check each index, and check every index after to see if there is a day that is warmer.

use a monotonic decreasing stack:
- monotonic: in decreasing order

- iterate through each element in the array
- pop elements from the stack as long as the current element is greater than the temperature at the index stored at the top of the stack
- push the current index onto the stack
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        # store indices of temperatures
        stack = []

        for index, temperature in enumerate(temperatures):
            # check if the current temperature is greater than the temperature at the index stored in the stack
            while stack and temperature > temperatures[stack[-1]]:
                # when temperature is greater, pop and calculate check previous indexes index difference (to find days where temp is smaller until hotter day which is current)
                stack_index = stack.pop()
                res[stack_index] = index - stack_index
            stack.append(index)
        return res
