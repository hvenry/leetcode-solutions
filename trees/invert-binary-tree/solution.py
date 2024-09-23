"""
invert a binary tree
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# time: O(n)
# space: O(h) where 'h' is the height of the tree
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        temp = root.left
        root.left = root.right
        root.right = temp

        # Recursively swap the left and right children of each node in the tree until reaching a leaf node (None)
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
