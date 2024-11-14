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

Optimal Solution O(n):
- construct an array that stores the times the paper was cited

citations:      [5, 1, 2, 8, 9, 3]
paper_counts:   [0, 1, 1, 1, 0, 1, 2]
                 0  1  2  3  4  5  >= 6

- go through the array backwards starting at n and compare the times the paper was cited to h (starting at a maximum of n)
- if the number of times that paper was cited is not h, then we lower the h index by one, check the second last element,
  and add to the total times of papers being cited.
- once the total number of papers cited is greater than h, we return h.

Complexity:
    Time: O(n)
    Space: O(n)
"""

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        # count the times the paper at was counted (index in paper_counts is the paper number)
        paper_counts = [0] * (n + 1)

        for c in citations:
            # min(n, c) makes the final element a "bucket"
            paper_counts[min(n, c)] += 1

        # our max h value could be n, so start here
        h = n
        papers = paper_counts[n]

        while papers < h:
            h -= 1
            papers += paper_counts[h]

        return h
