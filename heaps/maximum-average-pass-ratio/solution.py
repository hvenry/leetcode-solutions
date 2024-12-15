"""
Summary:
You are given a list classes, where classes[i] = [pass_i, total_i] and an integer extraStudents.

There are total_i students for the ith class, and there are class_i students that pass, and there
are extraStudents amount of students that can be added to anly class and are guaranteed to pass the
test.

The goal is to assign extraStudents to each class such that the passing ratio of students is maximized.

Example:
classes = [[1, 2], [3, 5], [2, 2]]
extraStudents = 2
returns: 0.78333

- To maximize the overall passing average, we can first assign 1 student to class 0, increasing the passing
  ratio from 0.5 -> 0.75, which is a gain of 0.25
- We can then maximize the overall passing average by increaseing class 0 from 2/3 to 3/4, which is a 0.08
  gain, which is the biggest achievable gain.

Solution:
- Use a min heap and store the gain to the passing ratio if a genuis student is added to the class
  (since we are using a min heap, this works because we want to minimize the greatest negative difference)
- For each student in extraStudents, pop a value from minheap, increment class size, calculate the gain, and put back into heap
- Return the average passing ratio of the processed heap

Complexity:
- Time: O(extraSudents log n)
- Space: O(n)
"""

from typing import List
import heapq


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> int:
        # calculate the potential from adding a genius student to each classroom
        h = [
            ((passes / tests) - ((passes + 1) / (tests + 1)), passes, tests)
            for passes, tests in classes
        ]
        heapq.heapify(h)

        # pop extraStudents amount from the heap
        for _ in range(extraStudents):
            gain, passes, total = heapq.heappop(h)

            # calculate the new gain of adding +1 to this classroom
            passes += 1
            total += 1
            gain = (passes / total) - ((passes + 1) / (total + 1))

            heapq.heappush(h, (gain, passes, total))

        # return the average lowest passing ratio after adding extraStudents
        return sum(passes / tests for _, passes, tests in h) / len(classes)
