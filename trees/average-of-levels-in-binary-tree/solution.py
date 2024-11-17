"""
Given the root of a binary tree, return the average value of the nodes on each level in
the form of an array. Answers within 10^-5 of the actual answer will be accepted.

Example 1:
        3
    9       20
          15  7

root = [3, 9, 20, null, null, 15, 7]
returns: [3.0, 14.5, 11.0]

The average of level 0 is 3
The average of level 1 is 14.5 ((9 + 20) / 2)
The average of level 2 is 11 ((15 + 7) / 2)

Solution:
- use a BFS, process 1 level at a time (iterate through length of our deque)
- keep track of an average, while also adding new subtrees to our queue
- append average / n (n being lenght of the dueque which is the lenght of our next level)
- return averages

Complexity:
- Time: O(n)
- Space: O(n)
"""

from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        averages = []
        q = deque()
        q.append(root)

        while q:
            average = 0
            # what is the length of the upcomming level?
            n = len(q)

            # process one level at a time
            for _ in range(n):
                node = q.popleft()
                average += node.val

                # setup next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            averages.append(average / n)

        return averages
