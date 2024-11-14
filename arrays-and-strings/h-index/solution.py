"""
Given an array of integers citations where citations[i] is the number of citations a researcher recieved for their ith
paper, return the researche's h-index.

According to the definition of h-index on wikipedia: The h-index is defined as the maximum value of h such that the given
researcher has published at least h papers that have each been cited at least h times.

Example 1:
citations = [3, 0, 6, 1, 5]
output = 3

[3, 0, 6, 1, 5] means the researcher has 5 papers in total and each of them had
recieved 3, 0, 6, 1, 5 citations respecitvely.

Since the researcher has 3 papers with at least 3 citations each and the remaining two with
no more than 3 citations each, their h-index is 3.


Naive Approach -> O(n^2):
keep testing from h = 0, iterating through all elements, and if the number is greater than h, add 1 to a count,
if the count is above h, then it is a valid value. We can keep doing this on h+=1, until h is no longer valid, resuling in the h-index.

Optimal Solution:



"""

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        h_index = 0

        for citation in citations:
            if citation >= n:
                h_index += 1

        return h_index
