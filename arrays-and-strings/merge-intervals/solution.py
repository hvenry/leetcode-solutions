from typing import List

"""
array of intervals with start and end value


intervals = [[1,3],[2,6],[8,10],[15,18]]
ans = [[1,6],[8,10],[15,18]]

sort intervals based off of start value

go to next start value, then next, to see if intervals overlap

return res
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start value, i[0]
        intervals.sort(key=lambda i: i[0])

        # base case
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                # max because [1, 5], [2, 4],
                # if we took the lower, we are making the interval smaller
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])

        return output
