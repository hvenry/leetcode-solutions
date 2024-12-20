"""
Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.

Return the root of the reversed tree.

A binary tree is perfect if all parent nodes have two children and all leaves are on the same leve.

The level of a node is the number of edges along the path between it and the root node.

Example:
root = [7, 13, 11]
returns: [7, 11, 13]

    7           ->          7
13      11              11      13

Solution:
- Use a bfs to traverse the tree for each level
- When the level is odd, we swap the the node values using a two pointers approach, reversing left and right

Complexity:
- Time: O(n)
- Space: O(n)
"""

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        level = 0

        # bfs
        while q:
            # if our level is odd, reverse values using two pointers
            if level & 1:
                left, right = 0, len(q) - 1
                while left < right:
                    q[left].val, q[right].val = q[right].val, q[left].val
                    left += 1
                    right -= 1

            # process each level of queue
            for _ in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        return root
