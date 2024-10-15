"""
Given the root of a binary tree, check whether it is a mirror of
itself (ie, symmetric around its center) (ie ie you can flip it).

example 1:
root = [1, 2, 2, 3, 4, 4, 3]

            1
    2               2
3       4       4       3

Returns True

example 2:
root = [1, 2, null, 3, null, 3]

            1
    2               2
        3               3

Returns False

Solution: Use DFS
- we explore the left and right subtress through a DFS
- If they both are none we return True
- If either of them do not exist, return False
-

Time: O(n)
Space: O(h) Worse case O(n) on call stack
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def same(root1, root2):
            # see of both are empty (symmetric)
            if not root1 and not root2:
                return True

            # mismatch (not symmetric)
            if not root1 or not root2:
                return False

            # if values are not the same, there is a mismatch
            if root1.val != root2.val:
                return False

            # We need to make sure this is true recusively
            # This is how we separate and traverse down the subtrees, making sure they are also symmetric
            return same(root1.left, root2.right) and same(root1.right, root2.left)

        return same(root, root)
