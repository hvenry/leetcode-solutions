"""
There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.

You are given two integer array position and speed, both of length n, where position[i] is the starting mile
of the ith car and speed[i] is the speed of the ith car in miles per hour.

A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.

A car fleet is a car or cars driving next to each other. The speed of the car fleet is the minimum speed of
any car in the fleet.

If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.

Return the number of car fleets that will arrive at the destination.

Example 1:
target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]

output = 3

- The car starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. The fleet forms at
  target. (10 + 2, 8 + 4)
- The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
- The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at
  speed 1 until it reaches target (5 + 1 = 6, 3 + 3 = 6)

    Therefore, we have a total of 3 fleets.

Intuition:
- Think about the problem as a system of linear equations. (position, speed)
    - The position is the y axis, the time is the x axis.
- The starting position is the y intercept, the speed is the ROC of the line
- When lines intercept, they become a fleet (we are looking for cars tha

Solution:
- We sort the inputs by their starting positions
- Use a monotonic decreasing stack, iterate through sorted car values
    - Calculate the time it takes to reach the destination for each car, add this time to the stack
    - When stack length is >= 2, we compare the newly added car to the car before it, if they collide with each other,
      remove the one that is at the top of the stack.
        - The cars collide with each other if the time of the previous car is less than the time of the next car

Complexity:
- Time: O(n log n)
- Space: O(n)
"""

from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]

        pairs.sort(reverse=True)
        stack = []

        for p, s in pairs:
            # calculate time until target
            time = (target - p) / s

            # append the calculated time to the stack
            stack.append(time)

            # Check if there is time overlap,
            # if there is they become a fleet (length of stack does not increase)
            # if there is not, they do not become a fleet (lenght stack and unqiue fleets increases)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
