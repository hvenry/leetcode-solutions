"""
Given the root of a binary search tree, and an integer k, return the kth
smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
root = [3, 1, 4, null, 2]
        3
    1       4
      2
k = 1

returns 1

Solution:
- we can do an in-order traversal and return the number at call k
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root

        while cur or stack:
            # keep going left (go as far left as possible) for in-order traversal
            while cur:
                # add previous values to stack
                stack.append(cur)
                cur = cur.left

            # once we are at the far left, now pop
            cur = stack.pop()

            # keep track of what number we are at to know when we are at k
            n += 1

            if n == k:
                return cur.val

            # pop from right when we need to
            cur = cur.right
