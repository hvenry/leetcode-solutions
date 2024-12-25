"""
Given the root of a binary tree, return an array of the largest value in each row
of the tree (0-indexed).

Example:
root = [1, 3, 2, 5, 3, null, 9]
        1
    3       2
   5 3       9

returns: [1, 3, 9]

Solution:
- Use a BFS to process each level of the tree
- Append the max of each level to result array

Complexity:
- Time: O(n)
- Space: O(n)
"""

from typing import Optional, List
from collections import deque
from math import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        q = deque([root])
        res = []

        # BFS using deque
        while q:
            cur_max = -inf

            for _ in range(len(q)):
                node = q.popleft()

                if node.val > cur_max:
                    cur_max = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # add max value from each level to result
            res.append(cur_max)

        return res
