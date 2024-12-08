"""
You are gievn a 0-indexed 2D integer array of events where events[i] = [startTime_i, endTime_i, value_i]. The ith
event starts at startTime_i and ends at endTime_i, and if you attend this event, you will recieve a value of value_i.
You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.

Return this maximum sum.

Example 1:
events = [[1, 3, 2], [4, 5, 2], [2, 4, 3]]

time    1  2  3  4  5
event 0 <----->       (1->3) value 2
event 1          <--> (4->5) value 2
event 2    <----->    (2->4) value 4

returns: 4
- we choose event 0 and 1 to get a total value of 4.

Intuition:
- Sort values by start times
- init best_previous to track best value from most recent non-overlapping events, best to the maximum value of any event
- our heap (priority queue) will manage events based on their end times
- iterate thruogh each event, and remove elements from the heap that end before the current event starts, updating best_previous
- add current events to the heap, and update best, then outside of the loop we can return the best value.

Optimal Solution:
- The optimal solution uses a binary search to solve the problem
- We sort the events based on their end times
- Track the max_until to know the max value of events to each end time
- Use bisect_left to perform a binary search to determine the maximum value of an evetn that ends before the current event starts


Complexity
- Time: O(n log n) -> maintaining heap, using bisect_left, sorting all have n log n complexity
- Space: O(n)
"""

from typing import List
import bisect
# import heapq


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # sort the vetns based on their end time
        events.sort(key=lambda x: x[1])

        # maintain a list of [endTime, max_value_until_now]
        max_until = []
        max_value = 0

        for _, e, v in events:
            max_value = max(max_value, v)
            max_until.append((e, max_value))

        # find maximum sum of two events
        result = 0

        for s, e, v in events:
            # option 1:  take the current event alone
            result = max(result, v)

            # option 2: take another event that ends before this one starts
            idx = bisect.bisect_left(max_until, (s, 0)) - 1

            if idx >= 0:
                result = max(result, v + max_until[idx][1])

        return result

        # # Heap solution
        # events.sort()
        # best_previous = float("-inf")
        #
        # best = max(v for _, _, v in events)
        #
        # h = []
        #
        # for s, e, v in events:
        #     # look for endings that are less than start
        #     while len(h) > 0 and h[0][0] <= s:
        #         _, nv = heapq.heappop(h)
        #         best_previous = max(best_previous, nv)
        #
        #     # add to heap the ending + 1 because there is no equal overlap allowed
        #     heapq.heappush(h, (e + 1, v))
        #     best = max(best, best_previous + v)
        #
        # return int(best)
